from pydantic import BaseModel, HttpUrl, UUID4
from pydantic_extra_types.color import Color


class Physical(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4
