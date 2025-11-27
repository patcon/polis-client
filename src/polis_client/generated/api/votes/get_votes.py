from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.vote import Vote
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    conversation_id: str,
    pid: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["conversation_id"] = conversation_id

    params["pid"] = pid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/votes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[Vote] | str | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_array_of_vote_item_data in _response_200:
            componentsschemas_array_of_vote_item = Vote.from_dict(
                componentsschemas_array_of_vote_item_data
            )

            response_200.append(componentsschemas_array_of_vote_item)

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[Vote] | str]:
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
    pid: int | Unset = UNSET,
) -> Response[list[Vote] | str]:
    """
    Args:
        conversation_id (str):
        pid (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Vote] | str]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        pid=pid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    conversation_id: str,
    pid: int | Unset = UNSET,
) -> list[Vote] | str | None:
    """
    Args:
        conversation_id (str):
        pid (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Vote] | str
    """

    return sync_detailed(
        client=client,
        conversation_id=conversation_id,
        pid=pid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    conversation_id: str,
    pid: int | Unset = UNSET,
) -> Response[list[Vote] | str]:
    """
    Args:
        conversation_id (str):
        pid (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Vote] | str]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        pid=pid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    conversation_id: str,
    pid: int | Unset = UNSET,
) -> list[Vote] | str | None:
    """
    Args:
        conversation_id (str):
        pid (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Vote] | str
    """

    return (
        await asyncio_detailed(
            client=client,
            conversation_id=conversation_id,
            pid=pid,
        )
    ).parsed
