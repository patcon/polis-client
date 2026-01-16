from polis_client.generated.models.comment import Comment
from polis_client.generated.models.conversation import Conversation
import pytest
import json
from pathlib import Path
from polis_client.client import PolisAPIError

@pytest.fixture
def expected_data(server_profile):
    snapshot_path = Path(__file__).parent / "__snapshots__"
    server_name = server_profile["name"]
    convo_id = server_profile["conversation_id"]
    report_id = server_profile["report_id"]

    comments_file = snapshot_path / f"{server_name}.comments.{convo_id}.expected.json"
    conversation_file = snapshot_path / f"{server_name}.conversation.{convo_id}.expected.json"
    math_file = snapshot_path / f"{server_name}.math.{convo_id}.expected.json"
    reports_file = snapshot_path / f"{server_name}.reports.{report_id}.expected.json"
    votes_file = snapshot_path / f"{server_name}.votes.{convo_id}.0.expected.json"
    init_file = snapshot_path / f"{server_name}.participationInit.{convo_id}.expected.json"

    return {
        "comments": json.loads(comments_file.read_text()),
        "conversation": json.loads(conversation_file.read_text()),
        "math": json.loads(math_file.read_text()),
        "reports": json.loads(reports_file.read_text()),
        "votes": json.loads(votes_file.read_text()),
        "participationInit": json.loads(init_file.read_text()),
    }

@pytest.mark.live_api
def test_live_api_get_comments_success(client, server_profile, expected_data):
    convo_id = server_profile["conversation_id"]
    expected_comments = expected_data["comments"]
    expected_comments = sorted(expected_comments, key=lambda d: d["tid"])
    expected_first_comment = expected_comments[0]

    comments = client.get_comments(conversation_id=convo_id)
    comments = sorted(comments, key=lambda c: c.tid)

    assert comments is not None
    if comments:
        assert all(isinstance(item, Comment) for item in comments)  

    actual_first_comment = comments[0]
    assert isinstance(actual_first_comment, Comment)
    assert actual_first_comment.to_dict() == expected_first_comment

@pytest.mark.live_api
def test_live_api_get_comments_nonexistent_convo_id(client):
    with pytest.raises(PolisAPIError, match="400: Bad Request"):
        client.get_comments(conversation_id="non-existent")

@pytest.mark.live_api
def test_live_api_get_conversation_success(client, server_profile, expected_data):
    convo_id = server_profile["conversation_id"]
    expected_conversation = expected_data["conversation"]

    convo = client.get_conversation(conversation_id=convo_id)

    assert isinstance(convo, Conversation)
    assert convo.to_dict() == expected_conversation

@pytest.mark.live_api
def test_live_api_get_conversation_nonexistent_convo_id(client):
    with pytest.raises(PolisAPIError, match="400: Bad Request"):
        client.get_conversation(conversation_id="non-existent")

@pytest.mark.live_api
def test_live_api_get_math_success(client, server_profile, expected_data):
    convo_id = server_profile["conversation_id"]
    expected_math = expected_data["math"]

    math = client.get_math(conversation_id=convo_id)

    assert math is not None
    assert sorted(expected_math.keys()) == sorted(math.to_dict().keys())
    assert sorted(expected_math) == sorted(math.to_dict())

@pytest.mark.live_api
def test_live_api_get_math_nonexistent_convo_id(client):
    with pytest.raises(PolisAPIError, match="400: Bad Request"):
        client.get_math(conversation_id="non-existent")

@pytest.mark.live_api
def test_live_api_get_votes_no_pid_success(client, server_profile):
    convo_id = server_profile["conversation_id"]
    votes = client.get_votes(conversation_id=convo_id)

    assert votes == []

@pytest.mark.live_api
def test_live_api_get_votes_success(client, server_profile, expected_data):
    convo_id = server_profile["conversation_id"]
    expected_first_vote = expected_data["votes"][0]

    votes = client.get_votes(conversation_id=convo_id, pid=0)

    assert votes is not None
    assert votes[0].to_dict() == expected_first_vote

@pytest.mark.live_api
def test_live_api_get_votes_nonexistent_convo_id(client):
    with pytest.raises(PolisAPIError, match="400: Bad Request"):
        client.get_votes(conversation_id="non-existent", pid=0)

@pytest.mark.live_api
def test_live_api_get_votes_nonexistent_pid(client, server_profile):
    convo_id = server_profile["conversation_id"]
    votes = client.get_votes(conversation_id=convo_id, pid=10000)

    assert votes == []

@pytest.mark.live_api
def test_live_api_get_report_success(client, server_profile, expected_data):
    report_id = server_profile["report_id"]
    expected_report = expected_data["reports"][0]

    report = client.get_report(report_id=report_id)

    assert report is not None
    assert report.to_dict() == expected_report

@pytest.mark.live_api
def test_live_api_get_report_nonexistent_report_id(client):
    with pytest.raises(PolisAPIError, match="400: Bad Request"):
        client.get_report(report_id="non-existent")

@pytest.mark.live_api
def test_live_api_get_export_file_success(client, server_profile):
    report_id = server_profile["report_id"]
    csv_text = client.get_export_file(
        report_id=report_id,
        filename="summary.csv",
    )

    assert isinstance(csv_text, str)
    assert csv_text.strip() != ""

@pytest.mark.live_api
def test_live_api_get_export_file_nonexistent_report_id(client):
    with pytest.raises(PolisAPIError, match="400: Bad Request"):
        client.get_export_file(
            report_id="non-existent",
            filename="summary.csv",
        )

@pytest.mark.live_api
def test_live_api_get_export_file_invalid_filename(client, server_profile):
    report_id = server_profile["report_id"]
    with pytest.raises(ValueError):
        client.get_export_file(
            report_id=report_id,
            filename="wrong.csv",
        )


@pytest.mark.live_api
def test_live_api_get_full_export_success(client, server_profile):
    report_id = server_profile["report_id"]
    exports = client.get_full_export(report_id=report_id)

    # Ensure correct shape
    assert isinstance(exports, dict)
    assert set(exports.keys()) == {
        "summary.csv",
        "comments.csv",
        "votes.csv",
        "participant-votes.csv",
        "comment-groups.csv",
    }

    # Ensure each file is populated
    for _, content in exports.items():
        assert isinstance(content, str)
        assert content.strip() != ""


@pytest.mark.live_api
def test_live_api_get_full_export_bad_report_id(client):
    with pytest.raises(PolisAPIError, match="400: Bad Request"):
        client.get_full_export(report_id="non-existent")

@pytest.mark.live_api
def test_live_api_get_initialization_success(client, server_profile, expected_data):
    convo_id = server_profile["conversation_id"]

    # Drop the nextComment key, since it varies each request.
    expected_init = expected_data["participationInit"]
    # expected_data["participationInit"]["nextComment"] = {}
    # expected_data["participationInit"]["acceptLanguage"] = "en-US"

    result = client.get_initialization(conversation_id=convo_id)
    actual_init = result.to_dict()
    # actual_init["nextComment"] = {}

    assert len(expected_init.keys()) == len(actual_init.keys())
    assert sorted(expected_init.keys()) == sorted(actual_init.keys())
    # Why we disable:
    # - Floating point values seem to update
    # - nextComment varies
    # assert expected_init == actual_init

@pytest.mark.live_api
def test_live_api_get_initialization_nonexistent_convo_id(client):
    with pytest.raises(PolisAPIError, match="400: Bad Request"):
        client.get_initialization(conversation_id="non-existent")

# TODO: Add live_api tests for get_participant method.

# TODO: Add live_api tests for participationInit with an xid.

# @pytest.mark.live_api
# def test_live_api_get_full_export_success():
#     client = PolisClient()
#     exports = client.get_full_export(report_id="r49xtpmxk2mjmkpyhwuau")

#     assert len(exports) == 5

# @pytest.mark.live_api
# def test_live_api_get_full_export_bad_report_id():
#     client = PolisClient()
#     with pytest.raises(APIError, match="Unexpected status 400 for get_full_export"):
#         client.get_full_export(report_id="non-existent")