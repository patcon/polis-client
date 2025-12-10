import pytest
from polis_client import PolisClient

@pytest.fixture
def client():
    return PolisClient()

def test_get_comments_defaults(mocker, client):
    mock_sync = mocker.patch(
        "polis_client.generated.api.comments.get_comments.sync",
        return_value="OK"
    )

    result = client.get_comments("2mock")

    assert result == "OK"
    mock_sync.assert_called_once_with(
        client=client,
        conversation_id="2mock",
        moderation=True,
        include_voting_patterns=True,
    )

def test_get_comments_defaults_override(mocker, client):
    mock_sync = mocker.patch(
        "polis_client.generated.api.comments.get_comments.sync",
        return_value="OK"
    )

    result = client.get_comments("2mock", moderation=False, include_voting_patterns=False)

    assert result == "OK"
    mock_sync.assert_called_once_with(
        client=client,
        conversation_id="2mock",
        moderation=False,
        include_voting_patterns=False,
    )