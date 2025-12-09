from polis_client.generated.models.math_v3 import MathV3
from .generated.client import Client as GeneratedClient
from .generated.api.comments import get_comments
from .generated.api.conversations import get_conversation
from .generated.api.math import get_math
from .generated.api.reports import get_report
from .generated.api.votes import get_votes
from .generated.models.comment import Comment
from .generated.models.conversation import Conversation
from .generated.models.report import Report
from .generated.models.vote import Vote
from .generated.types import Response
from typing import Any, List, Optional


class PolisAPIError(Exception):
    """Raised when the Polis API returns an error status code."""

    def __init__(self, status_code: int, content: bytes, message: Optional[str] = None):
        self.status_code = status_code
        self.content = content

        if message is None:
            content_str = content.decode('utf-8')
            message = f"Polis API returned status {status_code}: {content_str}"

        super().__init__(message)


class PolisClient:
    """Simple Polis API client wrapper around generated client code."""

    def __init__(self, base_url: str = "https://pol.is"):
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

        self._client = GeneratedClient(base_url=base)

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
        return get_comments.sync_detailed(
            client=self._client,
            conversation_id=conversation_id,
            moderation=moderation,
            include_voting_patterns=include_voting_patterns,
            **kwargs,
        )

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
        return get_votes.sync_detailed(
            client=self._client,
            conversation_id=conversation_id,
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
