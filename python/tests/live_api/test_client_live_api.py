from polis_client.generated.models.comment import Comment
from polis_client.generated.models.conversation import Conversation
import pytest
from polis_client.client4 import PolisAPIError, PolisClient

@pytest.fixture
def expected_data(server_profile):
    return server_profile["expected_data"]

@pytest.fixture
def math_keys():
    return {
        "base-clusters",
        "comment-priorities",
        "consensus",
        "group-aware-consensus",
        "group-clusters",
        "group-votes",
        "in-conv",
        "lastModTimestamp",
        "lastVoteTimestamp",
        "math_tick",
        "meta-tids",
        "mod-in",
        "mod-out",
        "n",
        "n-cmts",
        "pca",
        "repness",
        "tids",
        "user-vote-counts",
        "votes-base",
    }

@pytest.mark.live_api
def test_live_api_get_comments_success(client, server_profile, expected_data):
    convo_id = server_profile["conversation_id"]
    expected_first_comment = expected_data[convo_id]["first_comment"]

    comments = client.get_comments(conversation_id=convo_id)

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
    expected_conversation = expected_data[convo_id]["conversation"]

    convo = client.get_conversation(conversation_id=convo_id)

    assert isinstance(convo, Conversation)
    assert convo.to_dict() == expected_conversation

@pytest.mark.live_api
def test_live_api_get_conversation_nonexistent_convo_id(client):
    with pytest.raises(PolisAPIError, match="400: Bad Request"):
        client.get_conversation(conversation_id="non-existent")

@pytest.mark.live_api
def test_live_api_get_math_success(client, server_profile, math_keys):
    convo_id = server_profile["conversation_id"]
    expected_math_keys = math_keys

    math = client.get_math(conversation_id=convo_id)

    assert math is not None
    if math:
        assert sorted(expected_math_keys) == sorted(math.to_dict())

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
    expected_first_vote = expected_data[convo_id]["first_vote"]

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
    expected_report = expected_data[report_id]["report"]

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

# @pytest.mark.live_api
# def test_live_api_get_initialization_success():
#     client = PolisClient()
#     result = client.get_initialization(conversation_id="2demo")

#     expected_keys = [
#         'acceptLanguage',
#         'conversation',
#         'famous',
#         'nextComment',
#         'pca',
#         'ptpt',
#         'user',
#         'votes',
#     ]

#     assert len(expected_keys) == len(result.to_dict().keys())
#     assert sorted(result.to_dict().keys()) == sorted(expected_keys)

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