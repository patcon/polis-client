from enum import IntEnum


class ParticipantResponseMod(IntEnum):
    VALUE_NEGATIVE_1 = -1
    VALUE_0 = 0
    VALUE_1 = 1

    def __str__(self) -> str:
        return str(self.value)
