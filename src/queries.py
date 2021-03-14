import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="Some user"))

    @staticmethod
    def resolve_hello(parent, info, name):
        return f"Hello {name}"


