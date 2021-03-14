from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel, UUID4
from datetime import datetime


class User(BaseModel):
    id: UUID4
    name: str
    email: str
    phone: str
    created: datetime


class UserGrapheneModel(PydanticObjectType):
    class Meta:
        model = User

class UserGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = User
        exclude_fields = ("id", "created")



