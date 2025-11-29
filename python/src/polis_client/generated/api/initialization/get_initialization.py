from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.report import Report
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    conversation_id: str,
    xid: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["conversation_id"] = conversation_id

    params["xid"] = xid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/participationInit",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[Report] | str | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_array_of_report_item_data in _response_200:
            componentsschemas_array_of_report_item = Report.from_dict(
                componentsschemas_array_of_report_item_data
            )

            response_200.append(componentsschemas_array_of_report_item)

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
) -> Response[list[Report] | str]:
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
    xid: str | Unset = UNSET,
) -> Response[list[Report] | str]:
    """
    Args:
        conversation_id (str):
        xid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Report] | str]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        xid=xid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    conversation_id: str,
    xid: str | Unset = UNSET,
) -> list[Report] | str | None:
    """
    Args:
        conversation_id (str):
        xid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Report] | str
    """

    return sync_detailed(
        client=client,
        conversation_id=conversation_id,
        xid=xid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    conversation_id: str,
    xid: str | Unset = UNSET,
) -> Response[list[Report] | str]:
    """
    Args:
        conversation_id (str):
        xid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Report] | str]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        xid=xid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    conversation_id: str,
    xid: str | Unset = UNSET,
) -> list[Report] | str | None:
    """
    Args:
        conversation_id (str):
        xid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Report] | str
    """

    return (
        await asyncio_detailed(
            client=client,
            conversation_id=conversation_id,
            xid=xid,
        )
    ).parsed
