from django.contrib import admin
from django.urls import path,include
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
def flowers(request):
    flowers = Flower.objects.all()
    return flowers
@api.get("/vases", response=List[VaseSchema])
def vases(request):
    vases = Vase.objects.all()
    return vases
@api.get("/topics", response=List[TopicSchema])
def topics(request):
    topics = Topic.objects.all()
    return topics


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('generate.urls')),
    path("api/", api.urls),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)