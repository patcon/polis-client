from .generated.client import Client as GeneratedClient
from .generated.api.comments import get_comments
from .generated.api.conversations import get_conversation
from .generated.models.comment import Comment
from .generated.models.conversation import Conversation
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
    
    def __init__(self, base_url: str = "https://pol.is/api/v3"):
        """Initialize the Polis client.
        
        Args:
            base_url: Base URL for the Polis API. Defaults to https://pol.is/api/v3
        """
        self._client = GeneratedClient(base_url=base_url)
    
    def get_comments(self, conversation_id: str) -> Optional[List[Comment]]:
        """Get comments for a conversation, returning parsed Comment objects or raising on error.
        
        Args:
            conversation_id: The conversation ID to get comments for
            
        Returns:
            List of Comment objects if successful, None if no data
            
        Raises:
            PolisAPIError: If the API returns a non-2XX status code
            httpx.TimeoutException: If the request times out
        """
        response = self.get_comments_raw(conversation_id)
        
        # Check if status code is not 2XX
        if not (200 <= response.status_code < 300):
            raise PolisAPIError(response.status_code, response.content)
        
        return response.parsed
    
    def get_comments_raw(self, conversation_id: str) -> Response[Any | List[Comment]]:
        """Get comments for a conversation, returning full Response object.
        
        Args:
            conversation_id: The conversation ID to get comments for
            
        Returns:
            Response object with status_code, headers, content, and parsed data
        """
        return get_comments.sync_detailed(
            client=self._client,
            conversation_id=conversation_id
        )
    
    def get_conversation(self, conversation_id: str) -> Optional[Conversation]:
        """Get conversation details, returning parsed Conversation object or raising on error.
        
        Args:
            conversation_id: The conversation ID to get details for
            
        Returns:
            Conversation object if successful, None if no data
            
        Raises:
            PolisAPIError: If the API returns a non-2XX status code
            httpx.TimeoutException: If the request times out
        """
        response = self.get_conversation_raw(conversation_id)
        
        # Check if status code is not 2XX
        if not (200 <= response.status_code < 300):
            raise PolisAPIError(response.status_code, response.content)
        
        return response.parsed
    
    def get_conversation_raw(self, conversation_id: str) -> Response[Any | Conversation]:
        """Get conversation details, returning full Response object.
        
        Args:
            conversation_id: The conversation ID to get details for
            
        Returns:
            Response object with status_code, headers, content, and parsed data
        """
        return get_conversation.sync_detailed(
            client=self._client,
            conversation_id=conversation_id
        )