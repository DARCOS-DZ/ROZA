from django.shortcuts import render
from .models import *
import json

def index(request):
    #/flowers=[{flower_id:id,quantity=q},...]&vase_id=id&topic_id=id
    if "flower" in request.GET:
        flowers = request.GET.getlist("flower")#[{flower_id:id,quantity=q},...]
        vase_id = request.GET.get("vase") # vase_id = id
        topic_id = request.GET.get("topic")# topic_id = id
        array_of_flowers=[]
        print(flowers)
        for flower in flowers :
            print(flower)
            flower=json.loads(flower)
            # get flower object from database
            try:
                flower_object = Flower.objects.get(id=int(flower["flower_id"]))
            except Flower.DoesNotExist:
                flower_object = None
            # combining all flowers 3d obj path in one array
            if flower_object is not None:
                array_of_flowers.append({"flower":flower_object.object_3d.url,"quantity":flower["quantity"]})
        try:
            vase_obj = Vase.objects.get(id=int(vase_id)).object_3d
        except Vase.DoesNotExist:
            vase_obj=None
        try:
            topic_obj = Topic.objects.get(id=int(topic_id)).object_3d
        except Topic.DoesNotExist:
            topic_obj=None

        context= {
            "array_of_flowers":json.dumps(array_of_flowers),
            "vase_obj":vase_obj,
            "topic_obj":topic_obj
        }
        return render(request,"base.html",context)

    return render(request,"base.html")

