from pydantic import BaseModel, EmailStr
from pydantic.types import PastDate, FutureDate, List
from src.enums.user_enums import StatusesForPlayer
from pydantic.networks import IPv4Address, IPv6Address
from pydantic_extra_types.payment import PaymentCardNumber
from src.schemas.physical import Physical


"""
Именно в этом файле можно поиграться с уже готовой моделью и примером
тестового объекта для неё (Human).
"""

class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
    status: StatusesForPlayer
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo
