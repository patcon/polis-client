from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Conversation")


@_attrs_define
class Conversation:
    """
    Attributes:
        topic (str | Unset):
        description (str | Unset):
        is_anon (bool | Unset):
        is_active (bool | Unset):
        is_draft (bool | Unset):
        is_public (bool | Unset):
        created (int | Unset): Unix timestamp of report creation time Example: 1403054214174.
        modified (int | Unset): Unix timestamp of report modification time Example: 1403054214174.
    """

    topic: str | Unset = UNSET
    description: str | Unset = UNSET
    is_anon: bool | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_draft: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    created: int | Unset = UNSET
    modified: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        topic = self.topic

        description = self.description

        is_anon = self.is_anon

        is_active = self.is_active

        is_draft = self.is_draft

        is_public = self.is_public

        created = self.created

        modified = self.modified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if topic is not UNSET:
            field_dict["topic"] = topic
        if description is not UNSET:
            field_dict["description"] = description
        if is_anon is not UNSET:
            field_dict["is_anon"] = is_anon
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_draft is not UNSET:
            field_dict["is_draft"] = is_draft
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        topic = d.pop("topic", UNSET)

        description = d.pop("description", UNSET)

        is_anon = d.pop("is_anon", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_draft = d.pop("is_draft", UNSET)

        is_public = d.pop("is_public", UNSET)

        created = d.pop("created", UNSET)

        modified = d.pop("modified", UNSET)

        conversation = cls(
            topic=topic,
            description=description,
            is_anon=is_anon,
            is_active=is_active,
            is_draft=is_draft,
            is_public=is_public,
            created=created,
            modified=modified,
        )

        conversation.additional_properties = d
        return conversation

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
