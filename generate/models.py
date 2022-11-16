from django.db import models

# Create your models here.
class Flower(models.Model):
    reference=models.CharField(verbose_name="Reference name",unique=True,max_length=200)
    object_3d=models.FileField(verbose_name="3D Image",upload_to="flowers_obj",null=True,blank=True)
    def __str__(self):
        return self.reference
    
class Topic(models.Model):
    reference=models.CharField(verbose_name="reference",unique=True,max_length=200)
    object_3d=models.FileField(verbose_name="3D Image",upload_to="topics_obj",null=True,blank=True)
    def __str__(self):
        return self.reference
  
class Vase(models.Model):
    reference=models.CharField(verbose_name="reference",unique=True,max_length=200)
    object_3d=models.FileField(verbose_name="3D Image",upload_to="vases_obj",null=True,blank=True)
    max = models.PositiveIntegerField(verbose_name="max flowers",default=0)
    def __str__(self):
        return self.reference

class Position(models.Model):
    name = models.CharField("name", max_length=500)
    vase = models.ForeignKey("generate.Vase", on_delete=models.CASCADE)
    refernce_json_flowers = models.JSONField(null=True,blank=True)
    quantity = models.IntegerField("quantity")
    position_file = models.JSONField("position_file")
    def __str__(self):
        return self.name


