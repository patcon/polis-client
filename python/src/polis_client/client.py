from polis_client.generated.api.comments import create_comment
from polis_client.generated.api.conversations import get_conversation_uuid, get_conversation_xids_by_uuid
from polis_client.generated.api.initialization import get_initialization
from polis_client.generated.models.create_comment_body import CreateCommentBody
from polis_client.generated.models.create_vote_body import CreateVoteBody
from .generated.models.math_v3 import MathV3
from .generated.client import Client as GeneratedClient, AuthenticatedClient as GeneratedAuthenticatedClient
from .generated.api.comments import get_comments
from .generated.api.conversations import get_conversation
from .generated.api.exports import get_export_file
from .generated.api.math import get_math
from .generated.api.reports import get_report
from .generated.api.votes import get_votes, create_vote
from .generated.api.users import get_participant
from .generated.models.comment import Comment
from .generated.models.conversation import Conversation
from .generated.models.report import Report
from .generated.models.participant_response import ParticipantResponse
from .generated.models.participation_init import ParticipationInit
from .generated.models.vote import Vote
from .generated.models.get_export_file_filename import GetExportFileFilename
from .generated.types import UNSET, Response, Unset
from .errors import PolisAPIError
from typing import Any, List, Optional
import time
import base64
import json
import csv
import io


_ALLOWED_EXPORT_FILES: set[str] = {e.value for e in GetExportFileFilename}

def _decode_jwt(token: str) -> dict:
    """Decode JWT without verifying signature (we only need exp, xid, conversation_id)."""
    try:
        payload_b64 = token.split(".")[1]
        padded = payload_b64 + "=" * (-len(payload_b64) % 4)
        data = base64.urlsafe_b64decode(padded)
        return json.loads(data)
    except Exception:
        return {}

class PolisClient:
    """Simple Polis API client wrapper around generated client code."""

    def __init__(self, base_url: str = "https://pol.is", xid: Optional[str] = None, token: Optional[str] = None):
        """
        Initialize the Polis client.

        Args:
            base_url: Base URL for the Polis API. Can be:
                - "https://pol.is"
                - "https://pol.is/"
                - "https://pol.is/api/v3"
        """
        # Normalize: remove trailing slash
        base = base_url.rstrip("/")
        # If it already ends with /api/v3, keep it as-is
        if not base.endswith("/api/v3"):
            base = f"{base}/api/v3"

        self.base_url = base
        self._xid: str | Unset = UNSET if xid is None else xid
        self._token = token
        self._last_conversation_id: Optional[str] = None
        self._client: GeneratedClient | GeneratedAuthenticatedClient = GeneratedClient(base_url=base)

        self._initialize_from_token()

    def _update_last_conversation_id(self, conversation_id: str):
        if conversation_id and self._last_conversation_id != conversation_id:
            self._last_conversation_id = conversation_id

    def _initialize_from_token(self):
        """
        If a token is provided, decode it and extract stable fields
        such as xid and conversation_id. This runs only during __init__.
        """
        if not self._token:
            return

        try:
            payload = _decode_jwt(self._token)
        except Exception:
            return  # Token may be an opaque string or not a JWT yet

        xid = payload.get("xid")
        if xid:
            self._xid = xid

        conversation_id = payload.get("conversation_id")
        if conversation_id:
            self._last_conversation_id = conversation_id

    def _maybe_refresh_token(self):
        """
        Refresh token only if:
        - we have self._xid
        - we have self._last_conversation_id
        - token missing or expired
        """

        # Cannot refresh yet
        if not self._xid or not self._last_conversation_id:
            self._client = GeneratedClient(base_url=self.base_url)
            return

        # Determine if expired
        token_is_expired = True
        if self._token:
            payload = _decode_jwt(self._token)
            exp = payload.get("exp")
            token_is_expired = not exp or time.time() > exp

        if token_is_expired:
            # Fetch new token using get_initialization
            init_response = get_initialization.sync_detailed(
                client=self._client,
                conversation_id=self._last_conversation_id,
                xid=self._xid,
            )
            init = init_response.parsed

            auth_obj = getattr(init, "auth", None)
            self._token = getattr(auth_obj, "token", None) if auth_obj else None

        # Still no token → unauthenticated mode
        if not self._token:
            self._client = GeneratedClient(base_url=self.base_url)
            return

        # Token present → authenticated client
        self._client = GeneratedAuthenticatedClient(
            base_url=self.base_url,
            token=self._token,
        )

    def get_comments(self, **kwargs) -> Optional[List[Comment]]:
        """Get comments for a conversation, returning parsed Comment objects or raising on error.

        Args:
            conversation_id: The conversation ID to get comments for

        Returns:
            List of Comment objects if successful, None if no data

        Raises:
            PolisAPIError: If the API returns a non-2XX status code
            httpx.TimeoutException: If the request times out
        """
        response = self.get_comments_raw(**kwargs)

        # Check if status code is not 2XX
        if not (200 <= response.status_code < 300):
            raise PolisAPIError(response.status_code, response.content)

        return response.parsed

    def get_comments_raw(
        self,
        conversation_id: str,
        moderation: bool = True,
        include_voting_patterns: bool = True,
        **kwargs,
    ) -> Response[Any | List[Comment]]:
        """Get comments for a conversation, returning full Response object.

        Args:
            conversation_id: The conversation ID to get comments for

        Returns:
            Response object with status_code, headers, content, and parsed data
        """
        self._update_last_conversation_id(conversation_id)

        return get_comments.sync_detailed(
            client=self._client,
            conversation_id=conversation_id,
            moderation=moderation,
            include_voting_patterns=include_voting_patterns,
            **kwargs,
        )

    def get_participant(self, conversation_id: str, xid: str | Unset = UNSET, **kwargs) -> Optional[ParticipantResponse]:
        """Get conversation participant details.

        Args:
            conversation_id: conversation ID on which participant is scoped
            xid: external ID of the participant

        Returns:
            Participant object if successful.
        """
        response = get_participant.sync_detailed(
            client=self._client,
            conversation_id=conversation_id,
            xid=xid,
            **kwargs,
        )

        # Check if status code is not 2XX
        if not (200 <= response.status_code < 300):
            raise PolisAPIError(response.status_code, response.content)

        return response.parsed

    def get_conversation(self, conversation_id: str, **kwargs) -> Optional[Conversation]:
        """Get conversation details, returning parsed Conversation object or raising on error.

        Args:
            conversation_id: The conversation ID to get details for

        Returns:
            Conversation object if successful, None if no data

        Raises:
            PolisAPIError: If the API returns a non-2XX status code
            httpx.TimeoutException: If the request times out
        """
        response = self.get_conversation_raw(conversation_id, **kwargs)

        # Check if status code is not 2XX
        if not (200 <= response.status_code < 300):
            raise PolisAPIError(response.status_code, response.content)

        return response.parsed

    def get_conversation_raw(self, conversation_id: str, **kwargs) -> Response[Any | Conversation]:
        """Get conversation details, returning full Response object.

        Args:
            conversation_id: The conversation ID to get details for

        Returns:
            Response object with status_code, headers, content, and parsed data
        """
        self._update_last_conversation_id(conversation_id)

        return get_conversation.sync_detailed(
            client=self._client,
            conversation_id=conversation_id,
            **kwargs,
        )

    def get_math(self, conversation_id: str, **kwargs) -> Optional[Any | MathV3]:
        """
        """
        response = self.get_math_raw(conversation_id, **kwargs)

        # Check if status code is not 2XX
        if not (200 <= response.status_code < 300):
            raise PolisAPIError(response.status_code, response.content)

        return response.parsed

    def get_math_raw(self, conversation_id: str, **kwargs) -> Response[Any | MathV3]:
        self._update_last_conversation_id(conversation_id)

        return get_math.sync_detailed(
            client=self._client,
            conversation_id=conversation_id,
            **kwargs,
        )

    def get_votes(
        self,
        conversation_id: str,
        **kwargs,
    ) -> Optional[List[Vote]]:
        """Get votes for a conversation, returning parsed Vote objects or raising on error.

        Args:
            conversation_id: The conversation ID to get votes for

        Returns:
            List of Vote objects if successful, None if no data

        Raises:
            PolisAPIError: If the API returns a non-2XX status code
            httpx.TimeoutException: If the request times out
        """
        response = self.get_votes_raw(conversation_id=conversation_id, **kwargs)

        if not (200 <= response.status_code < 300):
            raise PolisAPIError(response.status_code, response.content)

        return response.parsed

    def get_votes_raw(
        self,
        conversation_id: str,
        **kwargs,
    ) -> Response[Any | List[Vote]]:
        """Get votes for a conversation, returning full Response object."""
        self._update_last_conversation_id(conversation_id)

        return get_votes.sync_detailed(
            client=self._client,
            conversation_id=conversation_id,
            **kwargs,
        )

    def create_vote(self, conversation_id: str, **kwargs):
        """
        """
        response = self.create_vote_raw(conversation_id=conversation_id, **kwargs)

        if not (200 <= response.status_code < 300):
            raise PolisAPIError(response.status_code, response.content)

        return response.parsed

    def create_vote_raw(self, conversation_id: str, **kwargs):
        """
        """
        self._update_last_conversation_id(conversation_id)
        self._maybe_refresh_token()

        if not isinstance(self._client, GeneratedAuthenticatedClient):
            raise

        return create_vote.sync_detailed(
            client=self._client,
            body=CreateVoteBody(conversation_id=conversation_id, **kwargs)
        )

    def create_comment(self, conversation_id: str, **kwargs):
        """
        """
        response = self.create_comment_raw(conversation_id=conversation_id, **kwargs)

        if not (200 <= response.status_code < 300):
            raise PolisAPIError(response.status_code, response.content)

        return response.parsed

    def create_comment_raw(self, conversation_id: str, **kwargs):
        """
        """
        self._update_last_conversation_id(conversation_id)
        self._maybe_refresh_token()

        if not isinstance(self._client, GeneratedAuthenticatedClient):
            raise

        return create_comment.sync_detailed(
            client=self._client,
            body=CreateCommentBody(conversation_id=conversation_id, **kwargs),
            **kwargs,
        )

    def get_report(
        self,
        report_id: str,
        **kwargs,
    ) -> Optional[Report]:
        """
        Get the report for a conversation, collapsing the returned list into a single object.

        Returns:
            Report object if successful, or None if no data.
        """
        response = self.get_report_raw(report_id=report_id, **kwargs)

        if not (200 <= response.status_code < 300):
            raise PolisAPIError(response.status_code, response.content)

        data = response.parsed

        if data is None:
            return None

        # The API returns a list, but we want a single object.
        if isinstance(data, list):
            if len(data) == 0:
                return None
            if len(data) >= 1:
                return data[0]

    def get_report_raw(
        self,
        report_id: str,
        **kwargs,
    ) -> Response[Any | List[Report]]:
        """Get the report for a conversation, returning full Response object."""
        return get_report.sync_detailed(
            client=self._client,
            report_id=report_id,
            **kwargs,
        )

    def get_initialization(
        self,
        conversation_id: str,
        **kwargs,
    ) -> Optional[ParticipationInit]:
        """
        """
        response = self.get_initialization_raw(conversation_id=conversation_id, **kwargs)

        if not (200 <= response.status_code < 300):
            raise PolisAPIError(response.status_code, response.content)

        return response.parsed

    def get_initialization_raw(
        self,
        conversation_id: str,
        **kwargs,
    ) -> Response[ParticipationInit]:
        """Get the participationInit response for a conversation."""
        self._update_last_conversation_id(conversation_id)

        return get_initialization.sync_detailed(
            client=self._client,
            conversation_id=conversation_id,
            xid=self._xid,
            **kwargs,
        )

    def get_export_file_raw(
        self,
        report_id: str,
        filename: str = "summary.csv",
        **kwargs,
    ) -> Response[str | None]:
        """
        Low-level: Get a CSV export file. Returns the full Response object.

        Parsed value is a raw CSV string or None.
        """

        if filename not in _ALLOWED_EXPORT_FILES:
            raise ValueError(
                f"Invalid export file '{filename}'. Must be one of: {sorted(_ALLOWED_EXPORT_FILES)}"
            )

        return get_export_file.sync_detailed(
            client=self._client,
            report_id=report_id,
            filename=filename,   # type: ignore (because generated type uses Literal[])
            **kwargs,
        )

    def get_export_file(
        self,
        report_id: str,
        filename: str = "summary.csv",
        **kwargs,
    ) -> str:
        """
        High-level helper: Download a CSV export file and return raw CSV text.

        Supported files:
            - summary.csv
            - comments.csv
            - votes.csv
            - participant-votes.csv
            - comment-groups.csv
            - comment-clusters.csv (maybe)
            - participant-importance.csv (maybe)
        """

        response = self.get_export_file_raw(
            report_id=report_id,
            filename=filename,
            **kwargs,
        )

        # Non-2XX → raise
        if not (200 <= response.status_code < 300):
            raise PolisAPIError(response.status_code, response.content)

        if response.parsed is None:
            raise RuntimeError(
                f"Expected CSV data but received None (report_id={report_id}, file={filename})"
            )

        return response.parsed


    # Convenience functions

    def get_full_export(self, report_id: str, **kwargs) -> dict[str, str]:
        """
        Download all CSV export files for a given report_id.

        Returns:
            {
                "summary.csv": "...",
                "comments.csv": "...",
                "votes.csv": "...",
                "participant-votes.csv": "...",
                "comment-groups.csv": "..."
            }
        """

        exports: dict[str, str] = {}

        for filename in _ALLOWED_EXPORT_FILES:
            exports[filename] = self.get_export_file(
                report_id=report_id,
                filename=filename,
                **kwargs,
            )

        return exports

    def get_xids(self, conversation_id: str):
        """
        A convenience function to get any xids associated with a conversation.

        This is a compound method that makes two API requests:
        get_conversation_uuid and get_conversation_xids_by_uuid

        It returns of list of dicts like so:

        ```
        [
            {"participant": "<pid>", "xid": "foobar"},
            {"participant": "<pid>", "xid": "foobar"},
            ...
        ]
        ```
        """
        self._update_last_conversation_id(conversation_id)
        self._maybe_refresh_token()

        if not self._token:
            # TODO: Raise a better exception, because we must be authenticated for this.
            raise

        conv_data = get_conversation_uuid.sync(client=self._client, conversation_id=conversation_id)
        conversation_uuid = getattr(conv_data, "conversation_uuid", None)
        if not conversation_uuid:
            raise ValueError(f"No conversation_uuid found for {conversation_id}")

        xids_csv = get_conversation_xids_by_uuid.sync(client=self._client, conversation_uuid=conversation_uuid)

        reader = csv.DictReader(io.StringIO(xids_csv))
        xid_rows = list(reader)

        return xid_rows

    def get_all_votes_slow(self, conversation_id: str):
        """
        A convenience function to get all votes for a conversation.

        This is a compound method that makes an API request for each participant,
        so it can be quite intensive on large conversations.

        If you have a report ID, you should instead fetch all votes with a single
        request to get_export_file(filename="votes.csv", ...).
        """
        math = self.get_math(conversation_id)
        if not math:
            raise

        n_participants = math.to_dict()["n"]
        all_votes = []

        for pid in range(n_participants):
            # Assuming you have a method like get_votes_for_participant
            participant_votes = self.get_votes(conversation_id, pid=pid)
            if participant_votes:
                all_votes.extend(participant_votes)

        return all_votes