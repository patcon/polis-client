from .generated.client import Client as GeneratedClient
from .generated.api.comments import get_comments
from .generated.api.conversations import get_conversation
from .generated.api.math import get_math
from .generated.api.reports import get_report
from .generated.api.votes import get_votes

DEFAULT_BASE_URL = "https://pol.is/api/v3"

def bind(client, fn):
    """Return a version of fn with `client` pre-filled."""
    return lambda *args, **kwargs: fn(*args, client=client, **kwargs)

class PolisClient(GeneratedClient):
    def __init__(self, base_url: str = DEFAULT_BASE_URL, **kwargs):
        super().__init__(base_url=base_url, **kwargs)

        # bind once, then use normally
        self.get_comments = bind(self, get_comments.sync)
        self.get_conversation = bind(self, get_conversation.sync)
        self.get_math = bind(self, get_math.sync)
        self.get_votes = bind(self, get_votes.sync)

        # custom wrapper for get_report to extract first element
        original_get_report = bind(self, get_report.sync)
        def get_report_first(*args, **kwargs):
            result = original_get_report(*args, **kwargs)
            if isinstance(result, list) and len(result) > 0:
                return result[0]
            return None

        self.get_report = get_report_first

