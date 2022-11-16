from django.shortcuts import render
from .models import *
import json


def index(request):
    #/flower=[{rose_id:id,quantity=q},...]&vase_id=id&topic_id=id
    if "flower" in request.GET:
        """*** GET user package data of flowers and topic"""
        flowers = request.GET.getlist("flower",None)#[{rose_id:id,quantity=q},...]
        vase_id = request.GET.get("vase",None) # vase_id = id
        topic_id = request.GET.get("topic",None)# topic_id = id
        total_quantity_flowers = 0
        array_of_flowers=[]
        array_json_flowers_from_user={}
        for flower in flowers :
            flower=json.loads(flower)
            # get flower object from database
            try:
                flower_object = Flower.objects.get(id=flower["rose_id"])
            except Flower.DoesNotExist:
                flower_object = None
            # combining all flowers 3d obj path in one array
            if flower_object is not None and flower_object.object_3d is not None:
                array_json_flowers_from_user.update({flower_object.reference:flower["quantity"]})
                total_quantity_flowers+=flower["quantity"] # count total quantity -> for filter get best position in vase
                for j in range(flower["quantity"]):
                    array_of_flowers.append(flower_object.object_3d.url)
        print(array_json_flowers_from_user)
        try:
            vase_obj = Vase.objects.get(id=vase_id)
        except Vase.DoesNotExist:
            vase_obj=None
        try:
            topic_obj = Topic.objects.get(id=topic_id)
        except Topic.DoesNotExist:
            topic_obj=None
        """
        handel get best position logic 
        /**********/
        """
        # 1 get user package data 
        # 2 
        try:
            best_position_json = Position.objects.filter(vase=vase_obj).first()
        except Position.DoesNotExist:
            best_position_json = None 
        print(best_position_json)
        context= {
            "array_of_flowers":json.dumps(array_of_flowers),
            "vase_obj":vase_obj,
            "topic_obj":topic_obj,
            "best_position_json":best_position_json,
        }
        return render(request,"base.html",context)

    return render(request,"base.html")

