from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.next_vote_translations_item import NextVoteTranslationsItem


T = TypeVar("T", bound="NextVote")


@_attrs_define
class NextVote:
    """
    Attributes:
        txt (str | Unset):
        tid (int | Unset):
        created (int | Unset):
        quote_src_url (None | str | Unset):
        is_seed (bool | Unset):
        is_meta (bool | Unset):
        lang (str | Unset):
        pid (int | Unset):
        random_n (float | Unset):
        remaining (int | Unset):
        total (int | Unset):
        translations (list[NextVoteTranslationsItem] | Unset):
        current_pid (int | Unset):
    """

    txt: str | Unset = UNSET
    tid: int | Unset = UNSET
    created: int | Unset = UNSET
    quote_src_url: None | str | Unset = UNSET
    is_seed: bool | Unset = UNSET
    is_meta: bool | Unset = UNSET
    lang: str | Unset = UNSET
    pid: int | Unset = UNSET
    random_n: float | Unset = UNSET
    remaining: int | Unset = UNSET
    total: int | Unset = UNSET
    translations: list[NextVoteTranslationsItem] | Unset = UNSET
    current_pid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        txt = self.txt

        tid = self.tid

        created = self.created

        quote_src_url: None | str | Unset
        if isinstance(self.quote_src_url, Unset):
            quote_src_url = UNSET
        else:
            quote_src_url = self.quote_src_url

        is_seed = self.is_seed

        is_meta = self.is_meta

        lang = self.lang

        pid = self.pid

        random_n = self.random_n

        remaining = self.remaining

        total = self.total

        translations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        current_pid = self.current_pid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if txt is not UNSET:
            field_dict["txt"] = txt
        if tid is not UNSET:
            field_dict["tid"] = tid
        if created is not UNSET:
            field_dict["created"] = created
        if quote_src_url is not UNSET:
            field_dict["quote_src_url"] = quote_src_url
        if is_seed is not UNSET:
            field_dict["is_seed"] = is_seed
        if is_meta is not UNSET:
            field_dict["is_meta"] = is_meta
        if lang is not UNSET:
            field_dict["lang"] = lang
        if pid is not UNSET:
            field_dict["pid"] = pid
        if random_n is not UNSET:
            field_dict["randomN"] = random_n
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if total is not UNSET:
            field_dict["total"] = total
        if translations is not UNSET:
            field_dict["translations"] = translations
        if current_pid is not UNSET:
            field_dict["currentPid"] = current_pid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.next_vote_translations_item import NextVoteTranslationsItem

        d = dict(src_dict)
        txt = d.pop("txt", UNSET)

        tid = d.pop("tid", UNSET)

        created = d.pop("created", UNSET)

        def _parse_quote_src_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quote_src_url = _parse_quote_src_url(d.pop("quote_src_url", UNSET))

        is_seed = d.pop("is_seed", UNSET)

        is_meta = d.pop("is_meta", UNSET)

        lang = d.pop("lang", UNSET)

        pid = d.pop("pid", UNSET)

        random_n = d.pop("randomN", UNSET)

        remaining = d.pop("remaining", UNSET)

        total = d.pop("total", UNSET)

        _translations = d.pop("translations", UNSET)
        translations: list[NextVoteTranslationsItem] | Unset = UNSET
        if _translations is not UNSET:
            translations = []
            for translations_item_data in _translations:
                translations_item = NextVoteTranslationsItem.from_dict(
                    translations_item_data
                )

                translations.append(translations_item)

        current_pid = d.pop("currentPid", UNSET)

        next_vote = cls(
            txt=txt,
            tid=tid,
            created=created,
            quote_src_url=quote_src_url,
            is_seed=is_seed,
            is_meta=is_meta,
            lang=lang,
            pid=pid,
            random_n=random_n,
            remaining=remaining,
            total=total,
            translations=translations,
            current_pid=current_pid,
        )

        next_vote.additional_properties = d
        return next_vote

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
