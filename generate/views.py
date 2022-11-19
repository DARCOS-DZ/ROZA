from django.shortcuts import render
from .models import *
import json

def combining_flowers(flower_object,array_json_flowers_from_user,flower,array_of_flowers):
    if flower_object is not None and flower_object.object_3d is not None:
        # get category name for filter database  EX : we get {'LILY': 11, 'HYDRANGE': 2}
        flower_key = flower_object.category.name
        """=== Append Array Elements with json object ==="""
        if flower_key in array_json_flowers_from_user:
            array_json_flowers_from_user.update({flower_key:flower["quantity"]+array_json_flowers_from_user[f"{flower_key}"]})
        else:
            array_json_flowers_from_user.update({flower_key:flower["quantity"]})
        for j in range(flower["quantity"]):
            array_of_flowers.append({'name':flower_key,'url':flower_object.object_3d.url})
        
def try_except_get_django_model(Model,id_name):
    try:
        model = Model.objects.get(id=id_name)
    except Model.DoesNotExist:
        model=None
    return model

def index(request):
    #/flower=[{rose_id:id,quantity=q},...]&vase_id=id&topic_id=id
    if "flower" and "vase" in request.GET:
        """*** GET user package data of flowers and topic"""
        flowers = request.GET.getlist("flower",None)#[{rose_id:id,quantity=q},...]
        vase_id = request.GET.get("vase",None) # vase_id = id
        topic_id = request.GET.get("topic",None)# topic_id = id
        array_of_flowers=[]
        topic = try_except_get_django_model(Topic,topic_id)
        vase = try_except_get_django_model(Vase,vase_id)
        array_json_flowers_from_user={"topic":1}

        for flower in flowers :
            flower=json.loads(flower)
            # get flower object from database
            try:
                flower_object = Flower.objects.get(id=flower["rose_id"])
            except Flower.DoesNotExist:
                flower_object = None
            """=== combining all flowers 3d obj path in one array ===="""
            combining_flowers(flower_object,array_json_flowers_from_user,flower,array_of_flowers)
        array_of_flowers.append({'name':"topic",'url':topic.object_3d.url})
        
        """*** Sorting array for syncronizing index ***"""
        new_array_sorted = []
        for i in sorted(array_of_flowers, key=lambda d: d['name']):
            new_array_sorted.append(i["url"])

        try:
            print("array_json_flowers_from_user",array_json_flowers_from_user)
            best_position_json = Position.objects.filter(refernce_json_flowers=array_json_flowers_from_user).first()
        except Position.DoesNotExist:
            best_position_json = None 
        if best_position_json:
            print("best_position_json",best_position_json.position_file)
        else:
            print("best_position_json is None",)

        context= {
            "array_of_flowers":json.dumps(new_array_sorted ),
            "vase_obj": vase,
            "topic_obj":topic,
            "best_position_json":best_position_json,
        }
        return render(request,"base.html",context)

    return render(request,"base.html")

