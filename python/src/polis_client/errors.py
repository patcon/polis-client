from typing import Optional


class PolisAPIError(Exception):
    """Raised when the Polis API returns an error status code."""

    def __init__(self, status_code: int, content: bytes, message: Optional[str] = None):
        self.status_code = status_code
        self.content = content

        if message is None:
            content_str = content.decode('utf-8')
            message = f"Polis API returned status {status_code}: {content_str}"

        super().__init__(message)