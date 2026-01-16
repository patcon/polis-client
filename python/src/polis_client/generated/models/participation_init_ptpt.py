from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.participant_response_mod import ParticipantResponseMod
from ..types import UNSET, Unset

T = TypeVar("T", bound="ParticipationInitPtpt")


@_attrs_define
class ParticipationInitPtpt:
    """
    Attributes:
        pid (int | Unset):
        uid (int | Unset):
        zid (int | Unset):
        vote_count (int | Unset):
        last_interaction (str | Unset):
        subscribed (int | Unset):
        last_notified (str | Unset):
        nsli (int | Unset):
        mod (ParticipantResponseMod | Unset): Moderation status of comment: moderated _out_ (-1), _not yet_ moderated
            (0), or moderated _in_ (1).
        created (str | Unset):
    """

    pid: int | Unset = UNSET
    uid: int | Unset = UNSET
    zid: int | Unset = UNSET
    vote_count: int | Unset = UNSET
    last_interaction: str | Unset = UNSET
    subscribed: int | Unset = UNSET
    last_notified: str | Unset = UNSET
    nsli: int | Unset = UNSET
    mod: ParticipantResponseMod | Unset = UNSET
    created: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pid = self.pid

        uid = self.uid

        zid = self.zid

        vote_count = self.vote_count

        last_interaction = self.last_interaction

        subscribed = self.subscribed

        last_notified = self.last_notified

        nsli = self.nsli

        mod: int | Unset = UNSET
        if not isinstance(self.mod, Unset):
            mod = self.mod.value

        created = self.created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pid is not UNSET:
            field_dict["pid"] = pid
        if uid is not UNSET:
            field_dict["uid"] = uid
        if zid is not UNSET:
            field_dict["zid"] = zid
        if vote_count is not UNSET:
            field_dict["vote_count"] = vote_count
        if last_interaction is not UNSET:
            field_dict["last_interaction"] = last_interaction
        if subscribed is not UNSET:
            field_dict["subscribed"] = subscribed
        if last_notified is not UNSET:
            field_dict["last_notified"] = last_notified
        if nsli is not UNSET:
            field_dict["nsli"] = nsli
        if mod is not UNSET:
            field_dict["mod"] = mod
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pid = d.pop("pid", UNSET)

        uid = d.pop("uid", UNSET)

        zid = d.pop("zid", UNSET)

        vote_count = d.pop("vote_count", UNSET)

        last_interaction = d.pop("last_interaction", UNSET)

        subscribed = d.pop("subscribed", UNSET)

        last_notified = d.pop("last_notified", UNSET)

        nsli = d.pop("nsli", UNSET)

        _mod = d.pop("mod", UNSET)
        mod: ParticipantResponseMod | Unset
        if isinstance(_mod, Unset):
            mod = UNSET
        else:
            mod = ParticipantResponseMod(_mod)

        created = d.pop("created", UNSET)

        participation_init_ptpt = cls(
            pid=pid,
            uid=uid,
            zid=zid,
            vote_count=vote_count,
            last_interaction=last_interaction,
            subscribed=subscribed,
            last_notified=last_notified,
            nsli=nsli,
            mod=mod,
            created=created,
        )

        participation_init_ptpt.additional_properties = d
        return participation_init_ptpt

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
