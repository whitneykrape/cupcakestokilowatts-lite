import uuid
from typing import Optional
from pydantic import BaseModel, Field
from mongoengine import Document
from mongoengine.fields import (
    FloatField,
    StringField,
    ListField,
    URLField,
    ObjectIdField,
)

# https://github.com/graphql-python/graphene-mongo/blob/master/examples/django_mongoengine/bike/models.py

class Idea(Document):
    meta = {'collection': 'idea'}    
    ID = ObjectIdField()
    name = StringField()
    unitofenergy = StringField()

    def __str__(self):
        return self.name
    
    def categoriesMatching(self):
        return 'A %s is "%s"' % (self.name, self.category)

class IdeaCreate(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Don Quixote"
            }
        }


class IdeaUpdate(BaseModel):
    name: Optional[str]
    category: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Don Quixote"
            }
        }