import graphene

from schemas import (
    UserGrapheneModel,
    UserGrapheneInputModel
)

from models import User


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="Some user"))

    @staticmethod
    def resolve_hello(parent, info, name):
        return f"Hello {name}"

class CreateUser(graphene.Mutation):
    class Arguments:
        user_args = UserGrapheneInputModel()

    Output = UserGrapheneModel

    @staticmethod
    def mutate(parent, info, user_args):
        user = User(**user_args.dict())
        user.save()
        return user


