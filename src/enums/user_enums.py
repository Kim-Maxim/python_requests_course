from enum import Enum


class Genders(Enum):
    female = "female"
    male = "male"

class Statuses(Enum):
    inactive = "inactive"
    active = "active"

class StatusesForPlayer(Enum):
    INACTIVE= "INACTIVE"
    ACTIVE = "ACTIVE"
    BANNED = "BANNED"
    DELETED = "DELETED"

class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain @"
    