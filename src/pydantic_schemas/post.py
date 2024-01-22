from pydantic import BaseModel, field_validator, Field


class Post(BaseModel):
    # id: int
    id: int = Field(le=3)
    title: str
    # name: str = Field(alias="_name")

    # @field_validator("id")
    # def check_that_id_is_less_than_three(cls, v):
    #     if v > 3: 
    #         raise ValueError('Id is not less than three')
    #     else:
    #         return v
        

    # {'id': 1, 'title': 'Post 1', '_name': 'Igor'}