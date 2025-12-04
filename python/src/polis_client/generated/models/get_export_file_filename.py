from enum import Enum


class GetExportFileFilename(str, Enum):
    COMMENTS_CSV = "comments.csv"
    COMMENT_GROUPS_CSV = "comment-groups.csv"
    PARTICIPANT_VOTES_CSV = "participant-votes.csv"
    SUMMARY_CSV = "summary.csv"
    VOTES_CSV = "votes.csv"

    def __str__(self) -> str:
        return str(self.value)
