from django.shortcuts import render
from .models import *
def index(request):
    #/flowers=[{flower_id:id,quantity=q},...]&vase_id=id&topic_id=id
    if "flowers" in request.GET:
        flowers = request.GET.get("flowers")#[{flower_id:id,quantity=q},...]
        vase_id = request.GET.get("vase") # vase_id = id
        topic_id = request.GET.get("topic")# topic_id = id
        array_of_flowers=[]
        for flower in flowers :
            # get flower object from database
            try:
                flower_object = Flower.objects.get(id=flower["flower_id"])
            except Flower.DoesNotExist:
                flower_object = None
            # combining all flowers 3d obj path in one array
            if flower_object is not None:
                for i in range(1,int(flower.quantity),1):
                    array_of_flowers.append(flower_object.object_3d)
        try:
            vase_obj = Vase.objects.get(id=vase_id)
        except Vase.DoesNotExist:
            vase_obj=None
        try:
            topic_obj = Topic.objects.get(id=topic_id)
        except Topic.DoesNotExist:
            topic_obj=None
        context= {
            "array_of_flowers":array_of_flowers,
            "vase_obj":vase_obj,
            "topic_obj":topic_obj
        }
        return render(request,"base.html",context)

    return render(request,"base.html")

