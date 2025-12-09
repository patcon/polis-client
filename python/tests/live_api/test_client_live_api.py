from polis_client.generated.models.comment import Comment
from polis_client.generated.models.conversation import Conversation
import pytest
from polis_client.client4 import PolisAPIError, PolisClient

@pytest.fixture
def expected_data():
    return {
        "2demo": {
            "first_comment": {
                'conversation_id': '2demo',
                'txt': 'This is a game changer. The myriad of unintended consequences it too complex to really understand; even for restaurant veterans.\n',
                'tid': 1,
                'created':
                '1403054218578',
                'quote_src_url': None,
                'is_seed': False,
                'is_meta': False,
                'lang': 'en',
                'pid': 0,
                'velocity': 1,
                'mod': 1,
                'active': True,
                'agree_count': 86,
                'disagree_count': 38,
                'pass_count': 44,
                'count': 168,
            },
            "conversation": {
                'auth_needed_to_vote': False,
                'auth_needed_to_write': True,
                'auth_opt_allow_3rdparty': True,
                'auth_opt_fb': True,
                'auth_opt_tw': True,
                'bgcolor': None,
                'context': 'polis_test',
                'conversation_id': '2demo',
                'course_id': None,
                'dataset_explanation': None,
                'description': 'How do you think the new minimum wage law will affect Seattle? Will it be for the better or for the worse? Why?',
                'email_domain': None,
                'help_bgcolor': None,
                'help_color': None,
                'help_type': 1,
                'importance_enabled': False,
                'is_active': True,
                'is_anon': False,
                'is_curated': False,
                'is_data_open': True,
                'is_draft': False,
                'is_mod': False,
                'is_owner': False,
                'is_public': True,
                'link_url': None,
                'need_suzinvite': False,
                'org_id': 125,
                'owner': 125,
                'owner_sees_participation_stats': False,
                'ownername': 'Mike Bjorkegren',
                'parent_url': None,
                'participant_count': 6361,
                'prioritize_seed': False,
                'profanity_filter': True,
                'site_id': 'polis_site_id_mike_all2',
                'socialbtn_type': 1,
                'spam_filter': True,
                'strict_moderation': True,
                'style_btn': '',
                'subscribe_type': 1,
                'topic': '$15/hour',
                'translations': [],
                'treevite_enabled': False,
                'upvotes': 1,
                'use_xid_whitelist': False,
                'vis_type': 1,
                'write_hint_type': 1,
                'write_type': 1,
                'created': '1403054152585',
                'modified': '1764981306417000',
            },
            "math_keys": {
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
            },
            "first_vote": {
                'pid': 0,
                'tid': 0,
                'vote': 0,
                'weight_x_32767': 0,
                'modified': '1403054214196',
                'conversation_id': '2demo',
            },
        },
        "r49xtpmxk2mjmkpyhwuau": {
            "report": {
                "report_id": "r49xtpmxk2mjmkpyhwuau",
                "created": "1501757120502",
                "modified": "1501757120502",
                "label_x_neg": None,
                "label_y_neg": None,
                "label_y_pos": None,
                "label_x_pos": None,
                "label_group_0": None,
                "label_group_1": None,
                "label_group_2": None,
                "label_group_3": None,
                "label_group_4": None,
                "label_group_5": None,
                "label_group_6": None,
                "label_group_7": None,
                "label_group_8": None,
                "label_group_9": None,
                "report_name": None,
                "mod_level": -2,
                "conversation_id": "5psrv8bm2a"
            },
        },
    }

@pytest.mark.live_api
def test_live_api_get_comments_success(expected_data):
    expected_first_comment = expected_data["2demo"]["first_comment"]

    client = PolisClient()
    comments = client.get_comments(conversation_id="2demo")

    assert comments is not None
    if comments:
        assert all(isinstance(item, Comment) for item in comments)  

    actual_first_comment = comments[0]
    assert isinstance(actual_first_comment, Comment)
    assert actual_first_comment.to_dict() == expected_first_comment

@pytest.mark.live_api
def test_live_api_get_comments_nonexistent_convo_id():
    client = PolisClient()
    with pytest.raises(PolisAPIError, match="400: Bad Request"):
        client.get_comments(conversation_id="non-existent")

@pytest.mark.live_api
def test_live_api_get_conversation_success(expected_data):
    expected_conversation = expected_data["2demo"]["conversation"]

    client = PolisClient()
    convo = client.get_conversation(conversation_id="2demo")

    assert isinstance(convo, Conversation)
    assert convo.to_dict() == expected_conversation

@pytest.mark.live_api
def test_live_api_get_conversation_nonexistent_convo_id():
    client = PolisClient()
    with pytest.raises(PolisAPIError, match="400: Bad Request"):
        client.get_conversation(conversation_id="non-existent")

@pytest.mark.live_api
def test_live_api_get_math_success(expected_data):
    expected_math_keys = expected_data["2demo"]["math_keys"]

    client = PolisClient()
    math = client.get_math(conversation_id="2demo")

    assert math is not None
    if math:
        assert sorted(expected_math_keys) == sorted(math.to_dict())

@pytest.mark.live_api
def test_live_api_get_math_nonexistent_convo_id():
    client = PolisClient()
    with pytest.raises(PolisAPIError, match="400: Bad Request"):
        client.get_math(conversation_id="non-existent")

@pytest.mark.live_api
def test_live_api_get_votes_no_pid_success():
    client = PolisClient()
    votes = client.get_votes(conversation_id="2demo")

    assert votes == []

@pytest.mark.live_api
def test_live_api_get_votes_success(expected_data):
    expected_first_vote = expected_data["2demo"]["first_vote"]

    client = PolisClient()
    votes = client.get_votes(conversation_id="2demo", pid=0)

    assert votes is not None
    assert votes[0].to_dict() == expected_first_vote

@pytest.mark.live_api
def test_live_api_get_votes_nonexistent_convo_id():
    client = PolisClient()
    with pytest.raises(PolisAPIError, match="400: Bad Request"):
        client.get_votes(conversation_id="non-existent", pid=0)

@pytest.mark.live_api
def test_live_api_get_votes_nonexistent_pid():
    client = PolisClient()
    votes = client.get_votes(conversation_id="2demo", pid=10000)

    assert votes == []

@pytest.mark.live_api
def test_live_api_get_report_success(expected_data):
    expected_report = expected_data["r49xtpmxk2mjmkpyhwuau"]["report"]

    client = PolisClient()
    report = client.get_report(report_id="r49xtpmxk2mjmkpyhwuau")

    assert report is not None
    assert report.to_dict() == expected_report

@pytest.mark.live_api
def test_live_api_get_report_nonexistent_report_id():
    client = PolisClient()
    with pytest.raises(PolisAPIError, match="400: Bad Request"):
        client.get_report(report_id="non-existent")

@pytest.mark.live_api
def test_live_api_get_export_file_success():
    client = PolisClient()

    csv_text = client.get_export_file(
        report_id="r49xtpmxk2mjmkpyhwuau",
        filename="summary.csv",
    )

    assert isinstance(csv_text, str)
    assert csv_text.strip() != ""

@pytest.mark.live_api
def test_live_api_get_export_file_nonexistent_report_id():
    client = PolisClient()
    with pytest.raises(PolisAPIError, match="400: Bad Request"):
        client.get_export_file(
            report_id="non-existent",
            filename="summary.csv",
        )

@pytest.mark.live_api
def test_live_api_get_export_file_invalid_filename():
    client = PolisClient()
    with pytest.raises(ValueError):
        client.get_export_file(
            report_id="r49xtpmxk2mjmkpyhwuau",
            filename="wrong.csv",
        )


@pytest.mark.live_api
def test_live_api_get_full_export_success():
    client = PolisClient()
    exports = client.get_full_export(report_id="r49xtpmxk2mjmkpyhwuau")

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
def test_live_api_get_full_export_bad_report_id():
    client = PolisClient()
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