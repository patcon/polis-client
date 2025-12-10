from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vote_response_next_comment import VoteResponseNextComment


T = TypeVar("T", bound="VoteResponse")


@_attrs_define
class VoteResponse:
    """
    Attributes:
        current_pid (int | Unset):
        next_comment (VoteResponseNextComment | Unset):
    """

    current_pid: int | Unset = UNSET
    next_comment: VoteResponseNextComment | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_pid = self.current_pid

        next_comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_comment, Unset):
            next_comment = self.next_comment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_pid is not UNSET:
            field_dict["currentPid"] = current_pid
        if next_comment is not UNSET:
            field_dict["nextComment"] = next_comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vote_response_next_comment import VoteResponseNextComment

        d = dict(src_dict)
        current_pid = d.pop("currentPid", UNSET)

        _next_comment = d.pop("nextComment", UNSET)
        next_comment: VoteResponseNextComment | Unset
        if isinstance(_next_comment, Unset):
            next_comment = UNSET
        else:
            next_comment = VoteResponseNextComment.from_dict(_next_comment)

        vote_response = cls(
            current_pid=current_pid,
            next_comment=next_comment,
        )

        vote_response.additional_properties = d
        return vote_response

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
