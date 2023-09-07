import graphene

from graphene_mongo import MongoengineObjectType

from .models import Idea as IdeaModel

class Idea(MongoengineObjectType):
    class Meta:
        model = IdeaModel

class Query(graphene.ObjectType):
    ideas = graphene.List(Idea)
    
    def resolve_ideas(self, info):
    	return list(IdeaModel.objects.all())


schema = graphene.Schema(query = Query)