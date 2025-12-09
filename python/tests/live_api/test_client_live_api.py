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
        }
    }

@pytest.mark.live_api
def test_live_api_get_comments_success(expected_data):
    expected_first_comment = expected_data["2demo"]["first_comment"]

    client = PolisClient()
    result = client.get_comments(conversation_id="2demo")

    assert result is not None
    if result:
        assert all(isinstance(item, Comment) for item in result)  

    actual_first_comment = result[0]
    assert isinstance(actual_first_comment, Comment)
    assert actual_first_comment.to_dict() == expected_first_comment

@pytest.mark.live_api
def test_live_api_get_comments_nonexistent_convo_id():
    client = PolisClient()
    with pytest.raises(PolisAPIError):
        client.get_comments(conversation_id="non-existent")

@pytest.mark.live_api
def test_live_api_get_conversation_success(expected_data):
    expected_conversation = expected_data["2demo"]["conversation"]

    client = PolisClient()
    result = client.get_conversation(conversation_id="2demo")

    assert isinstance(result, Conversation)
    assert result.to_dict() == expected_conversation

@pytest.mark.live_api
def test_live_api_get_conversation_nonexistent_convo_id():
    client = PolisClient()
    with pytest.raises(PolisAPIError):
        client.get_conversation(conversation_id="non-existent")

# @pytest.mark.live_api
# def test_live_api_get_math_success():
#     client = PolisClient()
#     result = client.get_math(conversation_id="2demo")

#     expected_math_keys = [
#         "base-clusters",
#         "comment-priorities",
#         "consensus",
#         "group-aware-consensus",
#         "group-clusters",
#         "group-votes",
#         "in-conv",
#         "lastModTimestamp",
#         "lastVoteTimestamp",
#         "math_tick",
#         "meta-tids",
#         "mod-in",
#         "mod-out",
#         "n",
#         "n-cmts",
#         "pca",
#         "repness",
#         "tids",
#         "user-vote-counts",
#         "votes-base",
#     ]

#     assert len(expected_math_keys) == len(result.to_dict().keys())
#     assert sorted(expected_math_keys) == sorted(result.to_dict().keys())

# @pytest.mark.live_api
# def test_live_api_get_math_nonexistent_convo_id():
#     client = PolisClient()
#     with pytest.raises(APIError, match="Unexpected status 400 for get_math"):
#         client.get_math(conversation_id="non-existent")

# @pytest.mark.live_api
# def test_live_api_get_votes_no_pid_success():
#     client = PolisClient()
#     result = client.get_votes(conversation_id="2demo")

#     assert result == []

# @pytest.mark.live_api
# def test_live_api_get_votes_success():
#     client = PolisClient()
#     result = client.get_votes(conversation_id="2demo", pid=0)

#     expected_first_vote = {
#         'pid': 0,
#         'tid': 0,
#         'vote': 0,
#         'weight_x_32767': 0,
#         'modified': '1403054214196',
#         'conversation_id': '2demo',
#     }

#     assert len(result) > 0
#     assert result[0].to_dict() == expected_first_vote

# @pytest.mark.live_api
# def test_live_api_get_votes_nonexistent_convo_id():
#     client = PolisClient()
#     with pytest.raises(APIError, match="Unexpected status 400 for get_votes"):
#         client.get_votes(conversation_id="non-existent", pid=0)

# @pytest.mark.live_api
# def test_live_api_get_votes_nonexistent_pid():
#     client = PolisClient()
#     result = client.get_votes(conversation_id="2demo", pid=10000)
    
#     assert result == []

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