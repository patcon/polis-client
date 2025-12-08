from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comment_mod import CommentMod
from ..types import UNSET, Unset

T = TypeVar("T", bound="Comment")


@_attrs_define
class Comment:
    """
    Attributes:
        txt (str): Body text of the comment Example: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        tid (int): Numeric ID of comment Example: 12.
        created (int): Unix timestamp of comment creation time Example: 1403054214174.
        quote_src_url (None | str): URL for a quoted tweet Example: Lorem ipsum dolor sit amet, consectetur adipiscing
            elit.
        is_seed (bool): Whether comment is a seed comment from moderator Example: True.
        is_meta (bool): Whether comment has been marked as metadata by moderator
        lang (str): Language of submitted comment Example: en.
        pid (int): Conversation-specific numeric ID of participant
        velocity (float | Unset):  Default: 1.0.
        mod (CommentMod | Unset): Moderation status of comment: moderated _out_ (-1), _not yet_ moderated (0), or
            moderated _in_ (1). Default: CommentMod.VALUE_0.
        active (bool | Unset):
        agree_count (int | Unset):  Example: 75.
        disagree_count (int | Unset):  Example: 29.
        pass_count (int | Unset):  Example: 37.
        count (int | Unset):  Example: 141.
    """

    txt: str
    tid: int
    created: int
    quote_src_url: None | str
    is_seed: bool
    is_meta: bool
    lang: str
    pid: int
    velocity: float | Unset = 1.0
    mod: CommentMod | Unset = CommentMod.VALUE_0
    active: bool | Unset = UNSET
    agree_count: int | Unset = UNSET
    disagree_count: int | Unset = UNSET
    pass_count: int | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        txt = self.txt

        tid = self.tid

        created = self.created

        quote_src_url: None | str
        quote_src_url = self.quote_src_url

        is_seed = self.is_seed

        is_meta = self.is_meta

        lang = self.lang

        pid = self.pid

        velocity = self.velocity

        mod: int | Unset = UNSET
        if not isinstance(self.mod, Unset):
            mod = self.mod.value

        active = self.active

        agree_count = self.agree_count

        disagree_count = self.disagree_count

        pass_count = self.pass_count

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "txt": txt,
                "tid": tid,
                "created": created,
                "quote_src_url": quote_src_url,
                "is_seed": is_seed,
                "is_meta": is_meta,
                "lang": lang,
                "pid": pid,
            }
        )
        if velocity is not UNSET:
            field_dict["velocity"] = velocity
        if mod is not UNSET:
            field_dict["mod"] = mod
        if active is not UNSET:
            field_dict["active"] = active
        if agree_count is not UNSET:
            field_dict["agree_count"] = agree_count
        if disagree_count is not UNSET:
            field_dict["disagree_count"] = disagree_count
        if pass_count is not UNSET:
            field_dict["pass_count"] = pass_count
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        txt = d.pop("txt")

        tid = d.pop("tid")

        created = d.pop("created")

        def _parse_quote_src_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        quote_src_url = _parse_quote_src_url(d.pop("quote_src_url"))

        is_seed = d.pop("is_seed")

        is_meta = d.pop("is_meta")

        lang = d.pop("lang")

        pid = d.pop("pid")

        velocity = d.pop("velocity", UNSET)

        _mod = d.pop("mod", UNSET)
        mod: CommentMod | Unset
        if isinstance(_mod, Unset):
            mod = UNSET
        else:
            mod = CommentMod(_mod)

        active = d.pop("active", UNSET)

        agree_count = d.pop("agree_count", UNSET)

        disagree_count = d.pop("disagree_count", UNSET)

        pass_count = d.pop("pass_count", UNSET)

        count = d.pop("count", UNSET)

        comment = cls(
            txt=txt,
            tid=tid,
            created=created,
            quote_src_url=quote_src_url,
            is_seed=is_seed,
            is_meta=is_meta,
            lang=lang,
            pid=pid,
            velocity=velocity,
            mod=mod,
            active=active,
            agree_count=agree_count,
            disagree_count=disagree_count,
            pass_count=pass_count,
            count=count,
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
