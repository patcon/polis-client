from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.math_v3 import MathV3
    from ..models.math_v4_as_buffer_of_gzipped_json import MathV4AsBufferOfGzippedJson
    from ..models.math_v4_consensus import MathV4Consensus
    from ..models.math_v4_repness import MathV4Repness


T = TypeVar("T", bound="MathV4")


@_attrs_define
class MathV4:
    """
    Attributes:
        as_buffer_of_gzipped_json (MathV4AsBufferOfGzippedJson | Unset):
        as_pojo (MathV3 | Unset):
        as_json (str | Unset):
        consensus (MathV4Consensus | Unset):
        expiration (int | Unset):
        repness (MathV4Repness | Unset):
    """

    as_buffer_of_gzipped_json: MathV4AsBufferOfGzippedJson | Unset = UNSET
    as_pojo: MathV3 | Unset = UNSET
    as_json: str | Unset = UNSET
    consensus: MathV4Consensus | Unset = UNSET
    expiration: int | Unset = UNSET
    repness: MathV4Repness | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_buffer_of_gzipped_json: dict[str, Any] | Unset = UNSET
        if not isinstance(self.as_buffer_of_gzipped_json, Unset):
            as_buffer_of_gzipped_json = self.as_buffer_of_gzipped_json.to_dict()

        as_pojo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.as_pojo, Unset):
            as_pojo = self.as_pojo.to_dict()

        as_json = self.as_json

        consensus: dict[str, Any] | Unset = UNSET
        if not isinstance(self.consensus, Unset):
            consensus = self.consensus.to_dict()

        expiration = self.expiration

        repness: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repness, Unset):
            repness = self.repness.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if as_buffer_of_gzipped_json is not UNSET:
            field_dict["asBufferOfGzippedJson"] = as_buffer_of_gzipped_json
        if as_pojo is not UNSET:
            field_dict["asPOJO"] = as_pojo
        if as_json is not UNSET:
            field_dict["asJSON"] = as_json
        if consensus is not UNSET:
            field_dict["consensus"] = consensus
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if repness is not UNSET:
            field_dict["repness"] = repness

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.math_v3 import MathV3
        from ..models.math_v4_as_buffer_of_gzipped_json import (
            MathV4AsBufferOfGzippedJson,
        )
        from ..models.math_v4_consensus import MathV4Consensus
        from ..models.math_v4_repness import MathV4Repness

        d = dict(src_dict)
        _as_buffer_of_gzipped_json = d.pop("asBufferOfGzippedJson", UNSET)
        as_buffer_of_gzipped_json: MathV4AsBufferOfGzippedJson | Unset
        if isinstance(_as_buffer_of_gzipped_json, Unset):
            as_buffer_of_gzipped_json = UNSET
        else:
            as_buffer_of_gzipped_json = MathV4AsBufferOfGzippedJson.from_dict(
                _as_buffer_of_gzipped_json
            )

        _as_pojo = d.pop("asPOJO", UNSET)
        as_pojo: MathV3 | Unset
        if isinstance(_as_pojo, Unset):
            as_pojo = UNSET
        else:
            as_pojo = MathV3.from_dict(_as_pojo)

        as_json = d.pop("asJSON", UNSET)

        _consensus = d.pop("consensus", UNSET)
        consensus: MathV4Consensus | Unset
        if isinstance(_consensus, Unset):
            consensus = UNSET
        else:
            consensus = MathV4Consensus.from_dict(_consensus)

        expiration = d.pop("expiration", UNSET)

        _repness = d.pop("repness", UNSET)
        repness: MathV4Repness | Unset
        if isinstance(_repness, Unset):
            repness = UNSET
        else:
            repness = MathV4Repness.from_dict(_repness)

        math_v4 = cls(
            as_buffer_of_gzipped_json=as_buffer_of_gzipped_json,
            as_pojo=as_pojo,
            as_json=as_json,
            consensus=consensus,
            expiration=expiration,
            repness=repness,
        )

        math_v4.additional_properties = d
        return math_v4

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
