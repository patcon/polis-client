from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vote")


@_attrs_define
class Vote:
    """
    Attributes:
        pid (int | Unset):
        tid (int | Unset):
        vote (int | Unset):
        weight_x_32767 (int | Unset):
        modified (int | Unset): Unix timestamp of vote modification time Example: 1403054214174.
        conversation_id (str | Unset):
    """

    pid: int | Unset = UNSET
    tid: int | Unset = UNSET
    vote: int | Unset = UNSET
    weight_x_32767: int | Unset = UNSET
    modified: int | Unset = UNSET
    conversation_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pid = self.pid

        tid = self.tid

        vote = self.vote

        weight_x_32767 = self.weight_x_32767

        modified = self.modified

        conversation_id = self.conversation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pid is not UNSET:
            field_dict["pid"] = pid
        if tid is not UNSET:
            field_dict["tid"] = tid
        if vote is not UNSET:
            field_dict["vote"] = vote
        if weight_x_32767 is not UNSET:
            field_dict["weight_x_32767"] = weight_x_32767
        if modified is not UNSET:
            field_dict["modified"] = modified
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pid = d.pop("pid", UNSET)

        tid = d.pop("tid", UNSET)

        vote = d.pop("vote", UNSET)

        weight_x_32767 = d.pop("weight_x_32767", UNSET)

        modified = d.pop("modified", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        vote = cls(
            pid=pid,
            tid=tid,
            vote=vote,
            weight_x_32767=weight_x_32767,
            modified=modified,
            conversation_id=conversation_id,
        )

        vote.additional_properties = d
        return vote

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
