from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.comment import Comment
from ...models.create_comment_body import CreateCommentBody
from ...types import Response


def _get_kwargs(
    *,
    body: CreateCommentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/comments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[Comment] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_array_of_comment_item_data in _response_200:
            componentsschemas_array_of_comment_item = Comment.from_dict(
                componentsschemas_array_of_comment_item_data
            )

            response_200.append(componentsschemas_array_of_comment_item)

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
) -> Response[Any | list[Comment]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCommentBody,
) -> Response[Any | list[Comment]]:
    """Create comment

     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc interdum tristique neque, id
    sollicitudin tortor sollicitudin vitae.

    Args:
        body (CreateCommentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[Comment]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateCommentBody,
) -> Any | list[Comment] | None:
    """Create comment

     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc interdum tristique neque, id
    sollicitudin tortor sollicitudin vitae.

    Args:
        body (CreateCommentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[Comment]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCommentBody,
) -> Response[Any | list[Comment]]:
    """Create comment

     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc interdum tristique neque, id
    sollicitudin tortor sollicitudin vitae.

    Args:
        body (CreateCommentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[Comment]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateCommentBody,
) -> Any | list[Comment] | None:
    """Create comment

     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc interdum tristique neque, id
    sollicitudin tortor sollicitudin vitae.

    Args:
        body (CreateCommentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[Comment]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
