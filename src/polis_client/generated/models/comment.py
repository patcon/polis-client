from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Comment")


@_attrs_define
class Comment:
    """
    Attributes:
        txt (str): Body text of the comment Example: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        tid (int): Numeric ID of comment Example: 12.
        created (int | Unset): Unix timestamp of comment creation time Example: 1403054214174.
        is_seed (bool | Unset): Whether comment is a seed comment from moderator Example: True.
        is_meta (bool | Unset): Whether comment has been marked as metadata by moderator
        lang (str | Unset): Language of submitted comment Example: en.
        pid (int | Unset): Conversation-specific numeric ID of participant
    """

    txt: str
    tid: int
    created: int | Unset = UNSET
    is_seed: bool | Unset = UNSET
    is_meta: bool | Unset = UNSET
    lang: str | Unset = UNSET
    pid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        txt = self.txt

        tid = self.tid

        created = self.created

        is_seed = self.is_seed

        is_meta = self.is_meta

        lang = self.lang

        pid = self.pid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "txt": txt,
                "tid": tid,
            }
        )
        if created is not UNSET:
            field_dict["created"] = created
        if is_seed is not UNSET:
            field_dict["is_seed"] = is_seed
        if is_meta is not UNSET:
            field_dict["is_meta"] = is_meta
        if lang is not UNSET:
            field_dict["lang"] = lang
        if pid is not UNSET:
            field_dict["pid"] = pid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        txt = d.pop("txt")

        tid = d.pop("tid")

        created = d.pop("created", UNSET)

        is_seed = d.pop("is_seed", UNSET)

        is_meta = d.pop("is_meta", UNSET)

        lang = d.pop("lang", UNSET)

        pid = d.pop("pid", UNSET)

        comment = cls(
            txt=txt,
            tid=tid,
            created=created,
            is_seed=is_seed,
            is_meta=is_meta,
            lang=lang,
            pid=pid,
        )

        comment.additional_properties = d
        return comment

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
