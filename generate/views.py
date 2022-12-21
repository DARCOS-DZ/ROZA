from django.shortcuts import render

from generate.utils import try_except_get_django_model, while_get_position
from .models import *
import json

def combining_flowers(flower_object,array_json_flowers_from_user,flower,array_of_flowers):
    """
    combine or set position to user flowers choices
    """
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
        

def index(request):
    #/flower=[{rose_id:id,quantity=q},...]&vase_id=id&{topic_id:id,quantity=q}
    if "flower" and "vase" in request.GET:
        """*** GET user package data of flowers and topic ***"""
        flowers = request.GET.getlist("flower",None)#[{rose_id:id,quantity=q},...]
        vase_id = request.GET.get("vase",None) # vase_id = id
        topic_id = request.GET.get("topic",None)#&topic={"id":id,"quantity":3}
        topic = json.loads(topic_id)
        try:topic_obj = Topic.objects.get(id_reference=topic["id"])
        except Topic.DoesNotExist:topic_obj=None
        array_of_flowers=[]
        vase = try_except_get_django_model(Vase,vase_id)
        if vase:
            array_json_flowers_from_user={}
            for flower in flowers :
                flower=json.loads(flower)
                # get flower object from database
                try:
                    flower_object = Flower.objects.get(id_reference=flower["rose_id"])
                except Flower.DoesNotExist:
                    flower_object = None
                """=== combining all flowers 3d obj path in one array ===="""
                combining_flowers(flower_object,array_json_flowers_from_user,flower,array_of_flowers)
            """*** Sorting array for syncronizing index ***"""
            new_array_sorted = []
            """add topics to this array for combaining with flowers """
            for t in range(topic["quantity"]):
                array_of_flowers.append({'name':topic_obj.reference,'url':topic_obj.object_3d.url})
            """ add topic in position json"""
            array_json_flowers_from_user.update({topic_obj.reference:topic["quantity"]})
            print("position",array_json_flowers_from_user)
            for i in sorted(array_of_flowers, key=lambda d: d['name']):
                new_array_sorted.append(i["url"])
            array_json_flowers_from_user_sorted = dict(sorted(array_json_flowers_from_user.items()))# ->> for sync js data with python data sorted
            try:
                best_position_json = Position.objects.filter(refernce_json_flowers=array_json_flowers_from_user_sorted).first()
            except Position.DoesNotExist:
                best_position_json = None 
            print(array_json_flowers_from_user_sorted)
            #while_get_position(best_position_json,array_json_flowers_from_user_sorted)
            context= {
                "array_of_flowers":json.dumps(new_array_sorted ),
                "vase_obj": vase,
                "best_position_json":best_position_json,
            }
            return render(request,"base.html",context)
    return render(request,"base.html")

