import pytest

SERVER_PROFILES = {
    "polis": {
        "base_url": "https://pol.is",
        "conversation_id": "5psrv8bm2a",
        "report_id": "r49xtpmxk2mjmkpyhwuau",
    },
    "voxit": {
        "base_url": "https://voxit.sitra.fi",
        "conversation_id": "2asfdaahhy",
        "report_id": "r3ejacrc8wuakjvfrcant",
    },
    "crownshy": {
        "base_url": "https://poliscommunity.crown-shy.com",
        "conversation_id": "9a8zymfrdj",
        "report_id": "r5awdrrrfif2zz5rbisnr",
    },
}


@pytest.fixture(params=[pytest.param(name, id=name) for name in SERVER_PROFILES])
def server_profile(request):
    """Runs each test once per server profile."""
    profile = SERVER_PROFILES[request.param]
    profile["name"] = request.param
    return profile


@pytest.fixture
def client(server_profile):
    from polis_client.client import PolisClient
    return PolisClient(base_url=server_profile["base_url"])