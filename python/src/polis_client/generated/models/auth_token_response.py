from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthTokenResponse")


@_attrs_define
class AuthTokenResponse:
    """
    Attributes:
        token (str | Unset):
        token_type (str | Unset):
        expires_in (int | Unset):
    """

    token: str | Unset = UNSET
    token_type: str | Unset = UNSET
    expires_in: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        token_type = self.token_type

        expires_in = self.expires_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token", UNSET)

        token_type = d.pop("token_type", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        auth_token_response = cls(
            token=token,
            token_type=token_type,
            expires_in=expires_in,
        )

        auth_token_response.additional_properties = d
        return auth_token_response

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
