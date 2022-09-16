from ninja import NinjaAPI
from ninja import Schema,ModelSchema

from generate.models import *
api = NinjaAPI()

class FlowerSchema(ModelSchema):
    class Config:
        model = Flower
        model_fields = "__all__"
class VaseSchema(ModelSchema):
    class Config:
        model = Vase
        model_fields = "__all__"
class TopicSchema(ModelSchema):
    class Config:
        model = Topic
        model_fields = "__all__"

from typing import List

@api.get("/flowers", response=List[FlowerSchema])
def list_employees(request):
    flowers = Flower.objects.all()
    return flowers
@api.get("/vases", response=List[VaseSchema])
def list_employees(request):
    vases = Vase.objects.all()
    return vases
@api.get("/topics", response=List[TopicSchema])
def list_employees(request):
    topics = Topic.objects.all()
    return topics


from django.urls import path
urlpatterns = [
]
