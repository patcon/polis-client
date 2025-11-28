from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comment_mod_mod import CommentModMod
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentMod")


@_attrs_define
class CommentMod:
    """
    Attributes:
        txt (str): Body text of the comment Example: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        tid (int): Numeric ID of comment Example: 12.
        created (int | Unset): Unix timestamp of comment creation time Example: 1403054214174.
        is_seed (bool | Unset): Whether comment is a seed comment from moderator Example: True.
        is_meta (bool | Unset): Whether comment has been marked as metadata by moderator
        lang (str | Unset): Language of submitted comment Example: en.
        pid (int | Unset): Conversation-specific numeric ID of participant
        velocity (float | Unset):  Default: 1.0.
        mod (CommentModMod | Unset): Moderation status of comment: moderated _out_ (-1), _not yet_ moderated (0), or
            moderated _in_ (1). Default: CommentModMod.VALUE_0.
        active (bool | Unset):
        conversation_id (str | Unset):  Example: 2demo.
    """

    txt: str
    tid: int
    created: int | Unset = UNSET
    is_seed: bool | Unset = UNSET
    is_meta: bool | Unset = UNSET
    lang: str | Unset = UNSET
    pid: int | Unset = UNSET
    velocity: float | Unset = 1.0
    mod: CommentModMod | Unset = CommentModMod.VALUE_0
    active: bool | Unset = UNSET
    conversation_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        txt = self.txt

        tid = self.tid

        created = self.created

        is_seed = self.is_seed

        is_meta = self.is_meta

        lang = self.lang

        pid = self.pid

        velocity = self.velocity

        mod: int | Unset = UNSET
        if not isinstance(self.mod, Unset):
            mod = self.mod.value

        active = self.active

        conversation_id = self.conversation_id

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
        if velocity is not UNSET:
            field_dict["velocity"] = velocity
        if mod is not UNSET:
            field_dict["mod"] = mod
        if active is not UNSET:
            field_dict["active"] = active
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id

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

        velocity = d.pop("velocity", UNSET)

        _mod = d.pop("mod", UNSET)
        mod: CommentModMod | Unset
        if isinstance(_mod, Unset):
            mod = UNSET
        else:
            mod = CommentModMod(_mod)

        active = d.pop("active", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        comment_mod = cls(
            txt=txt,
            tid=tid,
            created=created,
            is_seed=is_seed,
            is_meta=is_meta,
            lang=lang,
            pid=pid,
            velocity=velocity,
            mod=mod,
            active=active,
            conversation_id=conversation_id,
        )

        comment_mod.additional_properties = d
        return comment_mod

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
