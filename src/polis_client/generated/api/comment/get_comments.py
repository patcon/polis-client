from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.comment import Comment
from ...models.comment_mod import CommentMod
from ...models.comment_mod_voting import CommentModVoting
from ...models.get_comments_mod import GetCommentsMod
from ...models.get_comments_mod_gt import GetCommentsModGt
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    conversation_id: str,
    moderation: bool | Unset = UNSET,
    include_voting_patterns: bool | Unset = False,
    include_social: bool | Unset = UNSET,
    mod: GetCommentsMod | Unset = UNSET,
    mod_gt: GetCommentsModGt | Unset = UNSET,
    report_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["conversation_id"] = conversation_id

    params["moderation"] = moderation

    params["include_voting_patterns"] = include_voting_patterns

    params["include_social"] = include_social

    json_mod: int | Unset = UNSET
    if not isinstance(mod, Unset):
        json_mod = mod.value

    params["mod"] = json_mod

    json_mod_gt: int | Unset = UNSET
    if not isinstance(mod_gt, Unset):
        json_mod_gt = mod_gt.value

    params["mod_gt"] = json_mod_gt

    params["report_id"] = report_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/comments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[Comment] | list[CommentMod] | list[CommentModVoting] | str | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> list[Comment] | list[CommentMod] | list[CommentModVoting]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for (
                    componentsschemas_array_of_comment_mod_voting_item_data
                ) in _response_200_type_0:
                    componentsschemas_array_of_comment_mod_voting_item = (
                        CommentModVoting.from_dict(
                            componentsschemas_array_of_comment_mod_voting_item_data
                        )
                    )

                    response_200_type_0.append(
                        componentsschemas_array_of_comment_mod_voting_item
                    )

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_1 = []
                _response_200_type_1 = data
                for (
                    componentsschemas_array_of_comment_mod_item_data
                ) in _response_200_type_1:
                    componentsschemas_array_of_comment_mod_item = CommentMod.from_dict(
                        componentsschemas_array_of_comment_mod_item_data
                    )

                    response_200_type_1.append(
                        componentsschemas_array_of_comment_mod_item
                    )

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            response_200_type_2 = []
            _response_200_type_2 = data
            for componentsschemas_array_of_comment_item_data in _response_200_type_2:
                componentsschemas_array_of_comment_item = Comment.from_dict(
                    componentsschemas_array_of_comment_item_data
                )

                response_200_type_2.append(componentsschemas_array_of_comment_item)

            return response_200_type_2

        response_200 = _parse_response_200(response.json())

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
) -> Response[list[Comment] | list[CommentMod] | list[CommentModVoting] | str]:
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
    moderation: bool | Unset = UNSET,
    include_voting_patterns: bool | Unset = False,
    include_social: bool | Unset = UNSET,
    mod: GetCommentsMod | Unset = UNSET,
    mod_gt: GetCommentsModGt | Unset = UNSET,
    report_id: str | Unset = UNSET,
) -> Response[list[Comment] | list[CommentMod] | list[CommentModVoting] | str]:
    """List comments

     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc interdum tristique neque, id
    sollicitudin tortor sollicitudin vitae.

    Args:
        conversation_id (str):
        moderation (bool | Unset):
        include_voting_patterns (bool | Unset):  Default: False.
        include_social (bool | Unset):
        mod (GetCommentsMod | Unset):
        mod_gt (GetCommentsModGt | Unset):
        report_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Comment] | list[CommentMod] | list[CommentModVoting] | str]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        moderation=moderation,
        include_voting_patterns=include_voting_patterns,
        include_social=include_social,
        mod=mod,
        mod_gt=mod_gt,
        report_id=report_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    conversation_id: str,
    moderation: bool | Unset = UNSET,
    include_voting_patterns: bool | Unset = False,
    include_social: bool | Unset = UNSET,
    mod: GetCommentsMod | Unset = UNSET,
    mod_gt: GetCommentsModGt | Unset = UNSET,
    report_id: str | Unset = UNSET,
) -> list[Comment] | list[CommentMod] | list[CommentModVoting] | str | None:
    """List comments

     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc interdum tristique neque, id
    sollicitudin tortor sollicitudin vitae.

    Args:
        conversation_id (str):
        moderation (bool | Unset):
        include_voting_patterns (bool | Unset):  Default: False.
        include_social (bool | Unset):
        mod (GetCommentsMod | Unset):
        mod_gt (GetCommentsModGt | Unset):
        report_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Comment] | list[CommentMod] | list[CommentModVoting] | str
    """

    return sync_detailed(
        client=client,
        conversation_id=conversation_id,
        moderation=moderation,
        include_voting_patterns=include_voting_patterns,
        include_social=include_social,
        mod=mod,
        mod_gt=mod_gt,
        report_id=report_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    conversation_id: str,
    moderation: bool | Unset = UNSET,
    include_voting_patterns: bool | Unset = False,
    include_social: bool | Unset = UNSET,
    mod: GetCommentsMod | Unset = UNSET,
    mod_gt: GetCommentsModGt | Unset = UNSET,
    report_id: str | Unset = UNSET,
) -> Response[list[Comment] | list[CommentMod] | list[CommentModVoting] | str]:
    """List comments

     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc interdum tristique neque, id
    sollicitudin tortor sollicitudin vitae.

    Args:
        conversation_id (str):
        moderation (bool | Unset):
        include_voting_patterns (bool | Unset):  Default: False.
        include_social (bool | Unset):
        mod (GetCommentsMod | Unset):
        mod_gt (GetCommentsModGt | Unset):
        report_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Comment] | list[CommentMod] | list[CommentModVoting] | str]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        moderation=moderation,
        include_voting_patterns=include_voting_patterns,
        include_social=include_social,
        mod=mod,
        mod_gt=mod_gt,
        report_id=report_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    conversation_id: str,
    moderation: bool | Unset = UNSET,
    include_voting_patterns: bool | Unset = False,
    include_social: bool | Unset = UNSET,
    mod: GetCommentsMod | Unset = UNSET,
    mod_gt: GetCommentsModGt | Unset = UNSET,
    report_id: str | Unset = UNSET,
) -> list[Comment] | list[CommentMod] | list[CommentModVoting] | str | None:
    """List comments

     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc interdum tristique neque, id
    sollicitudin tortor sollicitudin vitae.

    Args:
        conversation_id (str):
        moderation (bool | Unset):
        include_voting_patterns (bool | Unset):  Default: False.
        include_social (bool | Unset):
        mod (GetCommentsMod | Unset):
        mod_gt (GetCommentsModGt | Unset):
        report_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Comment] | list[CommentMod] | list[CommentModVoting] | str
    """

    return (
        await asyncio_detailed(
            client=client,
            conversation_id=conversation_id,
            moderation=moderation,
            include_voting_patterns=include_voting_patterns,
            include_social=include_social,
            mod=mod,
            mod_gt=mod_gt,
            report_id=report_id,
        )
    ).parsed
