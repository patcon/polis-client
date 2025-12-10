from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.math_v3_base_clusters import MathV3BaseClusters
    from ..models.math_v3_comment_priorities import MathV3CommentPriorities
    from ..models.math_v3_consensus import MathV3Consensus
    from ..models.math_v3_group_aware_consensus import MathV3GroupAwareConsensus
    from ..models.math_v3_group_clusters_item import MathV3GroupClustersItem
    from ..models.math_v3_group_votes import MathV3GroupVotes
    from ..models.math_v3_pca import MathV3Pca
    from ..models.math_v3_repness import MathV3Repness
    from ..models.math_v3_user_vote_counts import MathV3UserVoteCounts
    from ..models.math_v3_votes_base import MathV3VotesBase


T = TypeVar("T", bound="MathV3")


@_attrs_define
class MathV3:
    """
    Attributes:
        base_clusters (MathV3BaseClusters | Unset):
        comment_priorities (MathV3CommentPriorities | Unset):
        consensus (MathV3Consensus | Unset):
        group_aware_consensus (MathV3GroupAwareConsensus | Unset):
        group_clusters (list[MathV3GroupClustersItem] | Unset):
        group_votes (MathV3GroupVotes | Unset):
        in_conv (list[int] | Unset):
        last_mod_timestamp (Any | Unset):
        last_vote_timestamp (int | Unset):
        math_tick (int | Unset):
        meta_tids (list[int] | Unset):
        mod_in (list[int] | Unset):
        mod_out (list[int] | Unset):
        n (int | Unset):
        n_cmts (int | Unset):
        pca (MathV3Pca | Unset):
        repness (MathV3Repness | Unset):
        tids (list[int] | Unset):
        user_vote_counts (MathV3UserVoteCounts | Unset):
        votes_base (MathV3VotesBase | Unset):
    """

    base_clusters: MathV3BaseClusters | Unset = UNSET
    comment_priorities: MathV3CommentPriorities | Unset = UNSET
    consensus: MathV3Consensus | Unset = UNSET
    group_aware_consensus: MathV3GroupAwareConsensus | Unset = UNSET
    group_clusters: list[MathV3GroupClustersItem] | Unset = UNSET
    group_votes: MathV3GroupVotes | Unset = UNSET
    in_conv: list[int] | Unset = UNSET
    last_mod_timestamp: Any | Unset = UNSET
    last_vote_timestamp: int | Unset = UNSET
    math_tick: int | Unset = UNSET
    meta_tids: list[int] | Unset = UNSET
    mod_in: list[int] | Unset = UNSET
    mod_out: list[int] | Unset = UNSET
    n: int | Unset = UNSET
    n_cmts: int | Unset = UNSET
    pca: MathV3Pca | Unset = UNSET
    repness: MathV3Repness | Unset = UNSET
    tids: list[int] | Unset = UNSET
    user_vote_counts: MathV3UserVoteCounts | Unset = UNSET
    votes_base: MathV3VotesBase | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_clusters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_clusters, Unset):
            base_clusters = self.base_clusters.to_dict()

        comment_priorities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comment_priorities, Unset):
            comment_priorities = self.comment_priorities.to_dict()

        consensus: dict[str, Any] | Unset = UNSET
        if not isinstance(self.consensus, Unset):
            consensus = self.consensus.to_dict()

        group_aware_consensus: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_aware_consensus, Unset):
            group_aware_consensus = self.group_aware_consensus.to_dict()

        group_clusters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_clusters, Unset):
            group_clusters = []
            for group_clusters_item_data in self.group_clusters:
                group_clusters_item = group_clusters_item_data.to_dict()
                group_clusters.append(group_clusters_item)

        group_votes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_votes, Unset):
            group_votes = self.group_votes.to_dict()

        in_conv: list[int] | Unset = UNSET
        if not isinstance(self.in_conv, Unset):
            in_conv = self.in_conv

        last_mod_timestamp = self.last_mod_timestamp

        last_vote_timestamp = self.last_vote_timestamp

        math_tick = self.math_tick

        meta_tids: list[int] | Unset = UNSET
        if not isinstance(self.meta_tids, Unset):
            meta_tids = self.meta_tids

        mod_in: list[int] | Unset = UNSET
        if not isinstance(self.mod_in, Unset):
            mod_in = self.mod_in

        mod_out: list[int] | Unset = UNSET
        if not isinstance(self.mod_out, Unset):
            mod_out = self.mod_out

        n = self.n

        n_cmts = self.n_cmts

        pca: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pca, Unset):
            pca = self.pca.to_dict()

        repness: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repness, Unset):
            repness = self.repness.to_dict()

        tids: list[int] | Unset = UNSET
        if not isinstance(self.tids, Unset):
            tids = self.tids

        user_vote_counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_vote_counts, Unset):
            user_vote_counts = self.user_vote_counts.to_dict()

        votes_base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.votes_base, Unset):
            votes_base = self.votes_base.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_clusters is not UNSET:
            field_dict["base-clusters"] = base_clusters
        if comment_priorities is not UNSET:
            field_dict["comment-priorities"] = comment_priorities
        if consensus is not UNSET:
            field_dict["consensus"] = consensus
        if group_aware_consensus is not UNSET:
            field_dict["group-aware-consensus"] = group_aware_consensus
        if group_clusters is not UNSET:
            field_dict["group-clusters"] = group_clusters
        if group_votes is not UNSET:
            field_dict["group-votes"] = group_votes
        if in_conv is not UNSET:
            field_dict["in-conv"] = in_conv
        if last_mod_timestamp is not UNSET:
            field_dict["lastModTimestamp"] = last_mod_timestamp
        if last_vote_timestamp is not UNSET:
            field_dict["lastVoteTimestamp"] = last_vote_timestamp
        if math_tick is not UNSET:
            field_dict["math_tick"] = math_tick
        if meta_tids is not UNSET:
            field_dict["meta-tids"] = meta_tids
        if mod_in is not UNSET:
            field_dict["mod-in"] = mod_in
        if mod_out is not UNSET:
            field_dict["mod-out"] = mod_out
        if n is not UNSET:
            field_dict["n"] = n
        if n_cmts is not UNSET:
            field_dict["n-cmts"] = n_cmts
        if pca is not UNSET:
            field_dict["pca"] = pca
        if repness is not UNSET:
            field_dict["repness"] = repness
        if tids is not UNSET:
            field_dict["tids"] = tids
        if user_vote_counts is not UNSET:
            field_dict["user-vote-counts"] = user_vote_counts
        if votes_base is not UNSET:
            field_dict["votes-base"] = votes_base

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.math_v3_base_clusters import MathV3BaseClusters
        from ..models.math_v3_comment_priorities import MathV3CommentPriorities
        from ..models.math_v3_consensus import MathV3Consensus
        from ..models.math_v3_group_aware_consensus import MathV3GroupAwareConsensus
        from ..models.math_v3_group_clusters_item import MathV3GroupClustersItem
        from ..models.math_v3_group_votes import MathV3GroupVotes
        from ..models.math_v3_pca import MathV3Pca
        from ..models.math_v3_repness import MathV3Repness
        from ..models.math_v3_user_vote_counts import MathV3UserVoteCounts
        from ..models.math_v3_votes_base import MathV3VotesBase

        d = dict(src_dict)
        _base_clusters = d.pop("base-clusters", UNSET)
        base_clusters: MathV3BaseClusters | Unset
        if isinstance(_base_clusters, Unset):
            base_clusters = UNSET
        else:
            base_clusters = MathV3BaseClusters.from_dict(_base_clusters)

        _comment_priorities = d.pop("comment-priorities", UNSET)
        comment_priorities: MathV3CommentPriorities | Unset
        if isinstance(_comment_priorities, Unset):
            comment_priorities = UNSET
        else:
            comment_priorities = MathV3CommentPriorities.from_dict(_comment_priorities)

        _consensus = d.pop("consensus", UNSET)
        consensus: MathV3Consensus | Unset
        if isinstance(_consensus, Unset):
            consensus = UNSET
        else:
            consensus = MathV3Consensus.from_dict(_consensus)

        _group_aware_consensus = d.pop("group-aware-consensus", UNSET)
        group_aware_consensus: MathV3GroupAwareConsensus | Unset
        if isinstance(_group_aware_consensus, Unset):
            group_aware_consensus = UNSET
        else:
            group_aware_consensus = MathV3GroupAwareConsensus.from_dict(
                _group_aware_consensus
            )

        _group_clusters = d.pop("group-clusters", UNSET)
        group_clusters: list[MathV3GroupClustersItem] | Unset = UNSET
        if _group_clusters is not UNSET:
            group_clusters = []
            for group_clusters_item_data in _group_clusters:
                group_clusters_item = MathV3GroupClustersItem.from_dict(
                    group_clusters_item_data
                )

                group_clusters.append(group_clusters_item)

        _group_votes = d.pop("group-votes", UNSET)
        group_votes: MathV3GroupVotes | Unset
        if isinstance(_group_votes, Unset):
            group_votes = UNSET
        else:
            group_votes = MathV3GroupVotes.from_dict(_group_votes)

        in_conv = cast(list[int], d.pop("in-conv", UNSET))

        last_mod_timestamp = d.pop("lastModTimestamp", UNSET)

        last_vote_timestamp = d.pop("lastVoteTimestamp", UNSET)

        math_tick = d.pop("math_tick", UNSET)

        meta_tids = cast(list[int], d.pop("meta-tids", UNSET))

        mod_in = cast(list[int], d.pop("mod-in", UNSET))

        mod_out = cast(list[int], d.pop("mod-out", UNSET))

        n = d.pop("n", UNSET)

        n_cmts = d.pop("n-cmts", UNSET)

        _pca = d.pop("pca", UNSET)
        pca: MathV3Pca | Unset
        if isinstance(_pca, Unset):
            pca = UNSET
        else:
            pca = MathV3Pca.from_dict(_pca)

        _repness = d.pop("repness", UNSET)
        repness: MathV3Repness | Unset
        if isinstance(_repness, Unset):
            repness = UNSET
        else:
            repness = MathV3Repness.from_dict(_repness)

        tids = cast(list[int], d.pop("tids", UNSET))

        _user_vote_counts = d.pop("user-vote-counts", UNSET)
        user_vote_counts: MathV3UserVoteCounts | Unset
        if isinstance(_user_vote_counts, Unset):
            user_vote_counts = UNSET
        else:
            user_vote_counts = MathV3UserVoteCounts.from_dict(_user_vote_counts)

        _votes_base = d.pop("votes-base", UNSET)
        votes_base: MathV3VotesBase | Unset
        if isinstance(_votes_base, Unset):
            votes_base = UNSET
        else:
            votes_base = MathV3VotesBase.from_dict(_votes_base)

        math_v3 = cls(
            base_clusters=base_clusters,
            comment_priorities=comment_priorities,
            consensus=consensus,
            group_aware_consensus=group_aware_consensus,
            group_clusters=group_clusters,
            group_votes=group_votes,
            in_conv=in_conv,
            last_mod_timestamp=last_mod_timestamp,
            last_vote_timestamp=last_vote_timestamp,
            math_tick=math_tick,
            meta_tids=meta_tids,
            mod_in=mod_in,
            mod_out=mod_out,
            n=n,
            n_cmts=n_cmts,
            pca=pca,
            repness=repness,
            tids=tids,
            user_vote_counts=user_vote_counts,
            votes_base=votes_base,
        )

        math_v3.additional_properties = d
        return math_v3

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
