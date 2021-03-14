import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from . import queries


app = FastAPI()

@app.get("/")
def root():
    return {"Fast": "Graph"}

app.add_route("/graph", GraphQLApp(schema=graphene.Schema(query=queries.Query)))



