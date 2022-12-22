from django.db import models
import requests
import json
BASE_API_ROSA="https://rosa.ae/app/v1/api"
# Create your models here.
class Flower(models.Model):
    reference=models.CharField(verbose_name="Reference name",unique=True,max_length=200)
    id_reference = models.IntegerField(null=True,blank=True)
    category = models.ForeignKey("generate.Category", on_delete=models.CASCADE,null=True)
    object_3d=models.FileField(verbose_name="3D Image",upload_to="flowers_obj",null=True,blank=True)
    def save(self, *args, **kwargs):
        if self.id_reference=="" or self.id_reference==None or not Flower.objects.filter(id_reference=self.id_reference).exists():
            try:
                rosa_api_flowers = requests.get(f"{BASE_API_ROSA}/get_rose")
                data =  json.loads (rosa_api_flowers.text)
                my_reference_name = self.reference.replace(' ','').upper()
                for flower in  data["data"]:
                    name = str(flower["name"]).replace(' ','').upper()
                    id_rosa_api = int(flower["id"])
                    if name == my_reference_name:
                        print("name",name,"id",id_rosa_api)
                        self.id_reference=id_rosa_api
            except Exception as e :
                print(e)
        super(Flower, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return self.reference
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name

class Topic(models.Model):
    id_reference = models.IntegerField(null=True,blank=True)
    reference=models.CharField(verbose_name="reference",unique=True,max_length=200)
    category = models.ForeignKey("generate.Category", on_delete=models.CASCADE,null=True)
    object_3d=models.FileField(verbose_name="3D Image",upload_to="topics_obj",null=True,blank=True)
    def __str__(self):
        return self.reference
    def save(self, *args, **kwargs):
        if self.id_reference=="" or self.id_reference==None or not Topic.objects.filter(id_reference=self.id_reference).exists():
            try:
                rosa_api_topics = requests.get(f"{BASE_API_ROSA}/get_gift_rose")
                data =  json.loads (rosa_api_topics.text)
                my_reference_name = self.reference.replace(' ','').upper()
                print(data)
                for topic in  data["data"]:
                    name = str(topic["name"]).replace(' ','').upper()
                    id_rosa_api = int(topic["id"])
                    if name == my_reference_name:
                        print("name",name,"id",id_rosa_api)
                        self.id_reference=id_rosa_api
            except Exception as e :
                print(e)
        super(Topic, self).save(*args, **kwargs) # Call the real save() method
class Vase(models.Model):
    reference=models.CharField(verbose_name="reference",unique=True,max_length=200)
    id_reference = models.IntegerField(null=True,blank=True)
    object_3d=models.FileField(verbose_name="3D Image",upload_to="vases_obj",null=True,blank=True)
    max = models.PositiveIntegerField(verbose_name="max flowers",default=0)
    def save(self, *args, **kwargs):
        if self.id_reference=="" or self.id_reference==None or not Vase.objects.filter(id_reference=self.id_reference).exists():
            try:
                rosa_api_vases = requests.get(f"{BASE_API_ROSA}/get_vase")
                data =  json.loads (rosa_api_vases.text)
                my_reference_name = self.reference.replace(' ','').upper()
                print(data)
                for vase in  data["data"]:
                    name = str(vase["name"]).replace(' ','').upper()
                    id_rosa_api = int(vase["id"])
                    if name == my_reference_name:
                        print("name",name,"id",id_rosa_api)
                        self.id_reference=id_rosa_api
            except Exception as e :
                print(e)
        super(Vase, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return self.reference

class Position(models.Model):
    name = models.CharField("name", max_length=500)
    vase = models.ForeignKey("generate.Vase", on_delete=models.CASCADE)
    vase_position = models.JSONField(null=True,blank=True)
    refernce_json_flowers = models.JSONField(null=True,blank=True)
    quantity = models.IntegerField("quantity")
    position_file = models.JSONField("position_file")
    rose_1 = models.CharField(max_length=100,null=True,blank=True)
    rose_2 = models.CharField(max_length=100,null=True,blank=True)
    rose_3 = models.CharField(max_length=100,null=True,blank=True)
    rose_4 = models.CharField(max_length=100,null=True,blank=True)
    quantity_1 = models.PositiveIntegerField(default=0)
    quantity_2 = models.PositiveIntegerField(default=0)
    quantity_3 = models.PositiveIntegerField(default=0)
    quantity_4 = models.PositiveIntegerField(default=0)
    def save(self, *args, **kwargs):
       reference_package = list(self.refernce_json_flowers)
       reference_package_quantity = list(self.refernce_json_flowers.values())
       if len(reference_package) == 4 :
        self.rose_1= reference_package[0]
        self.rose_2= reference_package[1]
        self.rose_3= reference_package[2]
        self.rose_3= reference_package[3]
        self.quantity_1= reference_package_quantity[0]
        self.quantity_2= reference_package_quantity[1]
        self.quantity_3= reference_package_quantity[2]
        self.quantity_3= reference_package_quantity[3]
       elif len(reference_package) == 3 :
        self.rose_1= reference_package[0]
        self.rose_2= reference_package[1]
        self.rose_3= reference_package[2]
        self.quantity_1= reference_package_quantity[0]
        self.quantity_2= reference_package_quantity[1]
        self.quantity_3= reference_package_quantity[2]
       elif len(reference_package) == 2 :
        self.rose_1= reference_package[0]
        self.rose_2= reference_package[1]
        self.quantity_1= reference_package_quantity[0]
        self.quantity_2= reference_package_quantity[1]
       elif len(reference_package) == 1 :
        self.rose_1= reference_package[0]
        self.quantity_1= reference_package_quantity[0]
       super(Position, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return self.name


