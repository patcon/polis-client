from typing import Optional

from polis_client.generated.models.participation_init import ParticipationInit
from .generated.client import Client as GeneratedClient
from .generated.api.comments import get_comments
from .generated.api.conversations import get_conversation
from .generated.api.math import get_math
from .generated.api.reports import get_report
from .generated.api.votes import get_votes
from .generated.api.initialization import get_initialization

DEFAULT_BASE_URL = "https://pol.is/api/v3"

def bind(client, fn):
    """Return a version of fn with `client` pre-filled."""
    return lambda *args, **kwargs: fn(*args, client=client, **kwargs)

class PolisClient(GeneratedClient):
    def __init__(self, base_url: str = DEFAULT_BASE_URL, xid: Optional[str] = None, **kwargs):
        super().__init__(base_url=base_url, **kwargs)

        self.token: str | None = None
        self.xid: str | None = xid

        # bind once, then use normally
        self.get_conversation = bind(self, get_conversation.sync)
        self.get_math = bind(self, get_math.sync)
        self.get_votes = bind(self, get_votes.sync)
        self.get_initialization = bind(self, get_initialization.sync)

        # custom wrapper for get_report to extract first element
        original_get_report = bind(self, get_report.sync)
        def get_report_first(*args, **kwargs):
            result = original_get_report(*args, **kwargs)
            if isinstance(result, list) and len(result) > 0:
                return result[0]
            return None

        self.get_report = get_report_first

    def _inject_auth(self):
        """Inject Authorization header if a token exists."""
        if self.token:
            self._headers["Authorization"] = f"Bearer {self.token}"

    def _ensure_token(self, conversation_id: str):
        """Lazy token creation; mirrors TS request interceptor logic."""
        if self.token:
            return
        if not self.xid:
            return  # cannot initialize without xid

        init = self.get_initialization(conversation_id=conversation_id, xid=self.xid)

        # Safely access nested attributes
        auth_obj = getattr(init, "auth", None)
        token_val = getattr(auth_obj, "token", None) if auth_obj else None
        self.token = token_val

        if self.token:
            self._inject_auth()

    def get_comments(
        self,
        conversation_id: str,
        moderation: bool = True,
        include_voting_patterns: bool = True,
        **kwargs,
    ):
        """
        Wrapper around the generated get_comments.sync to provide default values
        for moderation and include_voting_patterns, while still allowing overrides.
        """
        return get_comments.sync(
            client=self,
            conversation_id=conversation_id,
            moderation=moderation,
            include_voting_patterns=include_voting_patterns,
            **kwargs
        )