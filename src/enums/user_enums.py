from enum import Enum
from src.baseclasses.pyenum import PyEnum


class Genders(Enum):
    female = "female"
    male = "male"


class Statuses(Enum):
    inactive = "inactive"
    active = "active"


class StatusesForPlayer(PyEnum):
    INACTIVE = "INACTIVE"
    ACTIVE = "ACTIVE"
    BANNED = "BANNED"
    DELETED = "DELETED"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain @"
