from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_comment_body_vote import CreateCommentBodyVote
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCommentBody")


@_attrs_define
class CreateCommentBody:
    """
    Attributes:
        conversation_id (str):
        txt (str):
        is_seed (bool | Unset):
        vote (CreateCommentBodyVote | Unset):
    """

    conversation_id: str
    txt: str
    is_seed: bool | Unset = UNSET
    vote: CreateCommentBodyVote | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation_id = self.conversation_id

        txt = self.txt

        is_seed = self.is_seed

        vote: int | Unset = UNSET
        if not isinstance(self.vote, Unset):
            vote = self.vote.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversation_id": conversation_id,
                "txt": txt,
            }
        )
        if is_seed is not UNSET:
            field_dict["is_seed"] = is_seed
        if vote is not UNSET:
            field_dict["vote"] = vote

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversation_id = d.pop("conversation_id")

        txt = d.pop("txt")

        is_seed = d.pop("is_seed", UNSET)

        _vote = d.pop("vote", UNSET)
        vote: CreateCommentBodyVote | Unset
        if isinstance(_vote, Unset):
            vote = UNSET
        else:
            vote = CreateCommentBodyVote(_vote)

        create_comment_body = cls(
            conversation_id=conversation_id,
            txt=txt,
            is_seed=is_seed,
            vote=vote,
        )

        create_comment_body.additional_properties = d
        return create_comment_body

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
