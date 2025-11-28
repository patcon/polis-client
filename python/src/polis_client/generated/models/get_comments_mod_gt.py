from enum import IntEnum


class GetCommentsModGt(IntEnum):
    VALUE_NEGATIVE_1 = -1
    VALUE_0 = 0

    def __str__(self) -> str:
        return str(self.value)
