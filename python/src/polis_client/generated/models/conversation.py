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
        auth_needed_to_vote (str | Unset):
        auth_needed_to_write (str | Unset):
        auth_opt_allow_3rdparty (str | Unset):
        auth_opt_fb (str | Unset):
        auth_opt_tw (str | Unset):
        bgcolor (str | Unset):
        context (str | Unset):
        conversation_id (str | Unset):
        course_id (str | Unset):
        dataset_explanation (str | Unset):
        description (str | Unset):
        email_domain (str | Unset):
        help_bgcolor (str | Unset):
        help_color (str | Unset):
        help_type (str | Unset):
        importance_enabled (bool | Unset):
        is_active (bool | Unset):
        is_anon (bool | Unset):
        is_curated (bool | Unset):
        is_data_open (bool | Unset):
        is_draft (bool | Unset):
        is_mod (bool | Unset):
        is_owner (bool | Unset):
        is_public (bool | Unset):
        link_url (str | Unset):
        need_suzinvite (str | Unset):
        org_id (str | Unset):
        owner (str | Unset):
        owner_sees_participation_stats (str | Unset):
        ownername (str | Unset):
        parent_url (str | Unset):
        participant_count (str | Unset):
        prioritize_seed (str | Unset):
        profanity_filter (str | Unset):
        site_id (str | Unset):
        socialbtn_type (str | Unset):
        spam_filter (str | Unset):
        strict_moderation (str | Unset):
        style_btn (str | Unset):
        subscribe_type (str | Unset):
        topic (str | Unset):
        translations (str | Unset):
        treevite_enabled (bool | Unset):
        upvotes (str | Unset):
        use_xid_whitelist (str | Unset):
        vis_type (str | Unset):
        write_hint_type (str | Unset):
        write_type (str | Unset):
        created (int | Unset): Unix timestamp of report creation time Example: 1403054214174.
        modified (int | Unset): Unix timestamp of report modification time Example: 1403054214174.
    """

    auth_needed_to_vote: str | Unset = UNSET
    auth_needed_to_write: str | Unset = UNSET
    auth_opt_allow_3rdparty: str | Unset = UNSET
    auth_opt_fb: str | Unset = UNSET
    auth_opt_tw: str | Unset = UNSET
    bgcolor: str | Unset = UNSET
    context: str | Unset = UNSET
    conversation_id: str | Unset = UNSET
    course_id: str | Unset = UNSET
    dataset_explanation: str | Unset = UNSET
    description: str | Unset = UNSET
    email_domain: str | Unset = UNSET
    help_bgcolor: str | Unset = UNSET
    help_color: str | Unset = UNSET
    help_type: str | Unset = UNSET
    importance_enabled: bool | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_anon: bool | Unset = UNSET
    is_curated: bool | Unset = UNSET
    is_data_open: bool | Unset = UNSET
    is_draft: bool | Unset = UNSET
    is_mod: bool | Unset = UNSET
    is_owner: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    link_url: str | Unset = UNSET
    need_suzinvite: str | Unset = UNSET
    org_id: str | Unset = UNSET
    owner: str | Unset = UNSET
    owner_sees_participation_stats: str | Unset = UNSET
    ownername: str | Unset = UNSET
    parent_url: str | Unset = UNSET
    participant_count: str | Unset = UNSET
    prioritize_seed: str | Unset = UNSET
    profanity_filter: str | Unset = UNSET
    site_id: str | Unset = UNSET
    socialbtn_type: str | Unset = UNSET
    spam_filter: str | Unset = UNSET
    strict_moderation: str | Unset = UNSET
    style_btn: str | Unset = UNSET
    subscribe_type: str | Unset = UNSET
    topic: str | Unset = UNSET
    translations: str | Unset = UNSET
    treevite_enabled: bool | Unset = UNSET
    upvotes: str | Unset = UNSET
    use_xid_whitelist: str | Unset = UNSET
    vis_type: str | Unset = UNSET
    write_hint_type: str | Unset = UNSET
    write_type: str | Unset = UNSET
    created: int | Unset = UNSET
    modified: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_needed_to_vote = self.auth_needed_to_vote

        auth_needed_to_write = self.auth_needed_to_write

        auth_opt_allow_3rdparty = self.auth_opt_allow_3rdparty

        auth_opt_fb = self.auth_opt_fb

        auth_opt_tw = self.auth_opt_tw

        bgcolor = self.bgcolor

        context = self.context

        conversation_id = self.conversation_id

        course_id = self.course_id

        dataset_explanation = self.dataset_explanation

        description = self.description

        email_domain = self.email_domain

        help_bgcolor = self.help_bgcolor

        help_color = self.help_color

        help_type = self.help_type

        importance_enabled = self.importance_enabled

        is_active = self.is_active

        is_anon = self.is_anon

        is_curated = self.is_curated

        is_data_open = self.is_data_open

        is_draft = self.is_draft

        is_mod = self.is_mod

        is_owner = self.is_owner

        is_public = self.is_public

        link_url = self.link_url

        need_suzinvite = self.need_suzinvite

        org_id = self.org_id

        owner = self.owner

        owner_sees_participation_stats = self.owner_sees_participation_stats

        ownername = self.ownername

        parent_url = self.parent_url

        participant_count = self.participant_count

        prioritize_seed = self.prioritize_seed

        profanity_filter = self.profanity_filter

        site_id = self.site_id

        socialbtn_type = self.socialbtn_type

        spam_filter = self.spam_filter

        strict_moderation = self.strict_moderation

        style_btn = self.style_btn

        subscribe_type = self.subscribe_type

        topic = self.topic

        translations = self.translations

        treevite_enabled = self.treevite_enabled

        upvotes = self.upvotes

        use_xid_whitelist = self.use_xid_whitelist

        vis_type = self.vis_type

        write_hint_type = self.write_hint_type

        write_type = self.write_type

        created = self.created

        modified = self.modified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_needed_to_vote is not UNSET:
            field_dict["auth_needed_to_vote"] = auth_needed_to_vote
        if auth_needed_to_write is not UNSET:
            field_dict["auth_needed_to_write"] = auth_needed_to_write
        if auth_opt_allow_3rdparty is not UNSET:
            field_dict["auth_opt_allow_3rdparty"] = auth_opt_allow_3rdparty
        if auth_opt_fb is not UNSET:
            field_dict["auth_opt_fb"] = auth_opt_fb
        if auth_opt_tw is not UNSET:
            field_dict["auth_opt_tw"] = auth_opt_tw
        if bgcolor is not UNSET:
            field_dict["bgcolor"] = bgcolor
        if context is not UNSET:
            field_dict["context"] = context
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if course_id is not UNSET:
            field_dict["course_id"] = course_id
        if dataset_explanation is not UNSET:
            field_dict["dataset_explanation"] = dataset_explanation
        if description is not UNSET:
            field_dict["description"] = description
        if email_domain is not UNSET:
            field_dict["email_domain"] = email_domain
        if help_bgcolor is not UNSET:
            field_dict["help_bgcolor"] = help_bgcolor
        if help_color is not UNSET:
            field_dict["help_color"] = help_color
        if help_type is not UNSET:
            field_dict["help_type"] = help_type
        if importance_enabled is not UNSET:
            field_dict["importance_enabled"] = importance_enabled
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_anon is not UNSET:
            field_dict["is_anon"] = is_anon
        if is_curated is not UNSET:
            field_dict["is_curated"] = is_curated
        if is_data_open is not UNSET:
            field_dict["is_data_open"] = is_data_open
        if is_draft is not UNSET:
            field_dict["is_draft"] = is_draft
        if is_mod is not UNSET:
            field_dict["is_mod"] = is_mod
        if is_owner is not UNSET:
            field_dict["is_owner"] = is_owner
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if link_url is not UNSET:
            field_dict["link_url"] = link_url
        if need_suzinvite is not UNSET:
            field_dict["need_suzinvite"] = need_suzinvite
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if owner is not UNSET:
            field_dict["owner"] = owner
        if owner_sees_participation_stats is not UNSET:
            field_dict["owner_sees_participation_stats"] = (
                owner_sees_participation_stats
            )
        if ownername is not UNSET:
            field_dict["ownername"] = ownername
        if parent_url is not UNSET:
            field_dict["parent_url"] = parent_url
        if participant_count is not UNSET:
            field_dict["participant_count"] = participant_count
        if prioritize_seed is not UNSET:
            field_dict["prioritize_seed"] = prioritize_seed
        if profanity_filter is not UNSET:
            field_dict["profanity_filter"] = profanity_filter
        if site_id is not UNSET:
            field_dict["site_id"] = site_id
        if socialbtn_type is not UNSET:
            field_dict["socialbtn_type"] = socialbtn_type
        if spam_filter is not UNSET:
            field_dict["spam_filter"] = spam_filter
        if strict_moderation is not UNSET:
            field_dict["strict_moderation"] = strict_moderation
        if style_btn is not UNSET:
            field_dict["style_btn"] = style_btn
        if subscribe_type is not UNSET:
            field_dict["subscribe_type"] = subscribe_type
        if topic is not UNSET:
            field_dict["topic"] = topic
        if translations is not UNSET:
            field_dict["translations"] = translations
        if treevite_enabled is not UNSET:
            field_dict["treevite_enabled"] = treevite_enabled
        if upvotes is not UNSET:
            field_dict["upvotes"] = upvotes
        if use_xid_whitelist is not UNSET:
            field_dict["use_xid_whitelist"] = use_xid_whitelist
        if vis_type is not UNSET:
            field_dict["vis_type"] = vis_type
        if write_hint_type is not UNSET:
            field_dict["write_hint_type"] = write_hint_type
        if write_type is not UNSET:
            field_dict["write_type"] = write_type
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_needed_to_vote = d.pop("auth_needed_to_vote", UNSET)

        auth_needed_to_write = d.pop("auth_needed_to_write", UNSET)

        auth_opt_allow_3rdparty = d.pop("auth_opt_allow_3rdparty", UNSET)

        auth_opt_fb = d.pop("auth_opt_fb", UNSET)

        auth_opt_tw = d.pop("auth_opt_tw", UNSET)

        bgcolor = d.pop("bgcolor", UNSET)

        context = d.pop("context", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        course_id = d.pop("course_id", UNSET)

        dataset_explanation = d.pop("dataset_explanation", UNSET)

        description = d.pop("description", UNSET)

        email_domain = d.pop("email_domain", UNSET)

        help_bgcolor = d.pop("help_bgcolor", UNSET)

        help_color = d.pop("help_color", UNSET)

        help_type = d.pop("help_type", UNSET)

        importance_enabled = d.pop("importance_enabled", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_anon = d.pop("is_anon", UNSET)

        is_curated = d.pop("is_curated", UNSET)

        is_data_open = d.pop("is_data_open", UNSET)

        is_draft = d.pop("is_draft", UNSET)

        is_mod = d.pop("is_mod", UNSET)

        is_owner = d.pop("is_owner", UNSET)

        is_public = d.pop("is_public", UNSET)

        link_url = d.pop("link_url", UNSET)

        need_suzinvite = d.pop("need_suzinvite", UNSET)

        org_id = d.pop("org_id", UNSET)

        owner = d.pop("owner", UNSET)

        owner_sees_participation_stats = d.pop("owner_sees_participation_stats", UNSET)

        ownername = d.pop("ownername", UNSET)

        parent_url = d.pop("parent_url", UNSET)

        participant_count = d.pop("participant_count", UNSET)

        prioritize_seed = d.pop("prioritize_seed", UNSET)

        profanity_filter = d.pop("profanity_filter", UNSET)

        site_id = d.pop("site_id", UNSET)

        socialbtn_type = d.pop("socialbtn_type", UNSET)

        spam_filter = d.pop("spam_filter", UNSET)

        strict_moderation = d.pop("strict_moderation", UNSET)

        style_btn = d.pop("style_btn", UNSET)

        subscribe_type = d.pop("subscribe_type", UNSET)

        topic = d.pop("topic", UNSET)

        translations = d.pop("translations", UNSET)

        treevite_enabled = d.pop("treevite_enabled", UNSET)

        upvotes = d.pop("upvotes", UNSET)

        use_xid_whitelist = d.pop("use_xid_whitelist", UNSET)

        vis_type = d.pop("vis_type", UNSET)

        write_hint_type = d.pop("write_hint_type", UNSET)

        write_type = d.pop("write_type", UNSET)

        created = d.pop("created", UNSET)

        modified = d.pop("modified", UNSET)

        conversation = cls(
            auth_needed_to_vote=auth_needed_to_vote,
            auth_needed_to_write=auth_needed_to_write,
            auth_opt_allow_3rdparty=auth_opt_allow_3rdparty,
            auth_opt_fb=auth_opt_fb,
            auth_opt_tw=auth_opt_tw,
            bgcolor=bgcolor,
            context=context,
            conversation_id=conversation_id,
            course_id=course_id,
            dataset_explanation=dataset_explanation,
            description=description,
            email_domain=email_domain,
            help_bgcolor=help_bgcolor,
            help_color=help_color,
            help_type=help_type,
            importance_enabled=importance_enabled,
            is_active=is_active,
            is_anon=is_anon,
            is_curated=is_curated,
            is_data_open=is_data_open,
            is_draft=is_draft,
            is_mod=is_mod,
            is_owner=is_owner,
            is_public=is_public,
            link_url=link_url,
            need_suzinvite=need_suzinvite,
            org_id=org_id,
            owner=owner,
            owner_sees_participation_stats=owner_sees_participation_stats,
            ownername=ownername,
            parent_url=parent_url,
            participant_count=participant_count,
            prioritize_seed=prioritize_seed,
            profanity_filter=profanity_filter,
            site_id=site_id,
            socialbtn_type=socialbtn_type,
            spam_filter=spam_filter,
            strict_moderation=strict_moderation,
            style_btn=style_btn,
            subscribe_type=subscribe_type,
            topic=topic,
            translations=translations,
            treevite_enabled=treevite_enabled,
            upvotes=upvotes,
            use_xid_whitelist=use_xid_whitelist,
            vis_type=vis_type,
            write_hint_type=write_hint_type,
            write_type=write_type,
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
