from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateVoteBody")


@_attrs_define
class CreateVoteBody:
    """
    Attributes:
        conversation_id (str):
        tid (int):
        vote (int):
        high_priority (bool | Unset):
        lang (str | Unset):
        starred (bool | Unset):
    """

    conversation_id: str
    tid: int
    vote: int
    high_priority: bool | Unset = UNSET
    lang: str | Unset = UNSET
    starred: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation_id = self.conversation_id

        tid = self.tid

        vote = self.vote

        high_priority = self.high_priority

        lang = self.lang

        starred = self.starred

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversation_id": conversation_id,
                "tid": tid,
                "vote": vote,
            }
        )
        if high_priority is not UNSET:
            field_dict["high_priority"] = high_priority
        if lang is not UNSET:
            field_dict["lang"] = lang
        if starred is not UNSET:
            field_dict["starred"] = starred

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversation_id = d.pop("conversation_id")

        tid = d.pop("tid")

        vote = d.pop("vote")

        high_priority = d.pop("high_priority", UNSET)

        lang = d.pop("lang", UNSET)

        starred = d.pop("starred", UNSET)

        create_vote_body = cls(
            conversation_id=conversation_id,
            tid=tid,
            vote=vote,
            high_priority=high_priority,
            lang=lang,
            starred=starred,
        )

        create_vote_body.additional_properties = d
        return create_vote_body

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
