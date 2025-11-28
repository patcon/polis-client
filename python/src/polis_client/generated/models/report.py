from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Report")


@_attrs_define
class Report:
    """
    Attributes:
        report_id (str):
        created (int | Unset): Unix timestamp of report creation time Example: 1403054214174.
        modified (int | Unset): Unix timestamp of report modification time Example: 1403054214174.
        report_name (Any | Unset):
        mod_level (int | Unset):
        conversation_id (str | Unset):
    """

    report_id: str
    created: int | Unset = UNSET
    modified: int | Unset = UNSET
    report_name: Any | Unset = UNSET
    mod_level: int | Unset = UNSET
    conversation_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report_id = self.report_id

        created = self.created

        modified = self.modified

        report_name = self.report_name

        mod_level = self.mod_level

        conversation_id = self.conversation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "report_id": report_id,
            }
        )
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified
        if report_name is not UNSET:
            field_dict["report_name"] = report_name
        if mod_level is not UNSET:
            field_dict["mod_level"] = mod_level
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        report_id = d.pop("report_id")

        created = d.pop("created", UNSET)

        modified = d.pop("modified", UNSET)

        report_name = d.pop("report_name", UNSET)

        mod_level = d.pop("mod_level", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        report = cls(
            report_id=report_id,
            created=created,
            modified=modified,
            report_name=report_name,
            mod_level=mod_level,
            conversation_id=conversation_id,
        )

        report.additional_properties = d
        return report

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
