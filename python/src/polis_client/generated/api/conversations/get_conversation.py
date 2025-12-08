from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.conversation import Conversation
from ...types import UNSET, Response


def _get_kwargs(
    *,
    conversation_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["conversation_id"] = conversation_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/conversations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Conversation | None:
    if response.status_code == 200:
        response_200 = Conversation.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, response.text)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Conversation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    conversation_id: str,
) -> Response[Any | Conversation]:
    """
    Args:
        conversation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Conversation]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    conversation_id: str,
) -> Any | Conversation | None:
    """
    Args:
        conversation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Conversation
    """

    return sync_detailed(
        client=client,
        conversation_id=conversation_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    conversation_id: str,
) -> Response[Any | Conversation]:
    """
    Args:
        conversation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Conversation]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    conversation_id: str,
) -> Any | Conversation | None:
    """
    Args:
        conversation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Conversation
    """

    return (
        await asyncio_detailed(
            client=client,
            conversation_id=conversation_id,
        )
    ).parsed
