from enum import Enum, auto


class Validate(Enum):
    EMPTY = 1
    NOT_MATCH = 2
    VALID = 3


class FormMode(Enum):
    ADD = 0,
    EDIT = 1,
    DELETE = 2,
