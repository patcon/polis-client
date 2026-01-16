from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_token_response import AuthTokenResponse
    from ..models.conversation import Conversation
    from ..models.math_v4 import MathV4
    from ..models.participation_init_famous import ParticipationInitFamous
    from ..models.participation_init_next_comment import ParticipationInitNextComment
    from ..models.participation_init_ptpt import ParticipationInitPtpt
    from ..models.participation_init_user import ParticipationInitUser
    from ..models.participation_init_votes_item import ParticipationInitVotesItem


T = TypeVar("T", bound="ParticipationInit")


@_attrs_define
class ParticipationInit:
    """
    Attributes:
        accept_language (str | Unset):
        conversation (Conversation | Unset):
        famous (ParticipationInitFamous | Unset):
        next_comment (ParticipationInitNextComment | Unset):
        pca (MathV4 | str | Unset):
        ptpt (ParticipationInitPtpt | Unset):
        user (ParticipationInitUser | Unset):
        votes (list[ParticipationInitVotesItem] | Unset):
        auth (AuthTokenResponse | Unset):
    """

    accept_language: str | Unset = UNSET
    conversation: Conversation | Unset = UNSET
    famous: ParticipationInitFamous | Unset = UNSET
    next_comment: ParticipationInitNextComment | Unset = UNSET
    pca: MathV4 | str | Unset = UNSET
    ptpt: ParticipationInitPtpt | Unset = UNSET
    user: ParticipationInitUser | Unset = UNSET
    votes: list[ParticipationInitVotesItem] | Unset = UNSET
    auth: AuthTokenResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.math_v4 import MathV4

        accept_language = self.accept_language

        conversation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conversation, Unset):
            conversation = self.conversation.to_dict()

        famous: dict[str, Any] | Unset = UNSET
        if not isinstance(self.famous, Unset):
            famous = self.famous.to_dict()

        next_comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_comment, Unset):
            next_comment = self.next_comment.to_dict()

        pca: dict[str, Any] | str | Unset
        if isinstance(self.pca, Unset):
            pca = UNSET
        elif isinstance(self.pca, MathV4):
            pca = self.pca.to_dict()
        else:
            pca = self.pca

        ptpt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ptpt, Unset):
            ptpt = self.ptpt.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        votes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.votes, Unset):
            votes = []
            for votes_item_data in self.votes:
                votes_item = votes_item_data.to_dict()
                votes.append(votes_item)

        auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accept_language is not UNSET:
            field_dict["acceptLanguage"] = accept_language
        if conversation is not UNSET:
            field_dict["conversation"] = conversation
        if famous is not UNSET:
            field_dict["famous"] = famous
        if next_comment is not UNSET:
            field_dict["nextComment"] = next_comment
        if pca is not UNSET:
            field_dict["pca"] = pca
        if ptpt is not UNSET:
            field_dict["ptpt"] = ptpt
        if user is not UNSET:
            field_dict["user"] = user
        if votes is not UNSET:
            field_dict["votes"] = votes
        if auth is not UNSET:
            field_dict["auth"] = auth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_token_response import AuthTokenResponse
        from ..models.conversation import Conversation
        from ..models.math_v4 import MathV4
        from ..models.participation_init_famous import ParticipationInitFamous
        from ..models.participation_init_next_comment import (
            ParticipationInitNextComment,
        )
        from ..models.participation_init_ptpt import ParticipationInitPtpt
        from ..models.participation_init_user import ParticipationInitUser
        from ..models.participation_init_votes_item import ParticipationInitVotesItem

        d = dict(src_dict)
        accept_language = d.pop("acceptLanguage", UNSET)

        _conversation = d.pop("conversation", UNSET)
        conversation: Conversation | Unset
        if isinstance(_conversation, Unset):
            conversation = UNSET
        else:
            conversation = Conversation.from_dict(_conversation)

        _famous = d.pop("famous", UNSET)
        famous: ParticipationInitFamous | Unset
        if isinstance(_famous, Unset):
            famous = UNSET
        else:
            famous = ParticipationInitFamous.from_dict(_famous)

        _next_comment = d.pop("nextComment", UNSET)
        next_comment: ParticipationInitNextComment | Unset
        if isinstance(_next_comment, Unset):
            next_comment = UNSET
        else:
            next_comment = ParticipationInitNextComment.from_dict(_next_comment)

        def _parse_pca(data: object) -> MathV4 | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pca_type_0 = MathV4.from_dict(data)

                return pca_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MathV4 | str | Unset, data)

        pca = _parse_pca(d.pop("pca", UNSET))

        _ptpt = d.pop("ptpt", UNSET)
        ptpt: ParticipationInitPtpt | Unset
        if isinstance(_ptpt, Unset):
            ptpt = UNSET
        else:
            ptpt = ParticipationInitPtpt.from_dict(_ptpt)

        _user = d.pop("user", UNSET)
        user: ParticipationInitUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ParticipationInitUser.from_dict(_user)

        _votes = d.pop("votes", UNSET)
        votes: list[ParticipationInitVotesItem] | Unset = UNSET
        if _votes is not UNSET:
            votes = []
            for votes_item_data in _votes:
                votes_item = ParticipationInitVotesItem.from_dict(votes_item_data)

                votes.append(votes_item)

        _auth = d.pop("auth", UNSET)
        auth: AuthTokenResponse | Unset
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = AuthTokenResponse.from_dict(_auth)

        participation_init = cls(
            accept_language=accept_language,
            conversation=conversation,
            famous=famous,
            next_comment=next_comment,
            pca=pca,
            ptpt=ptpt,
            user=user,
            votes=votes,
            auth=auth,
        )

        participation_init.additional_properties = d
        return participation_init

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
