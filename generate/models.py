from django.db import models

# Create your models here.
class Flower(models.Model):
    name=models.CharField(verbose_name="Name",max_length=200)
    name_ar=models.CharField(verbose_name="Arabic name",max_length=200)
    image=models.ImageField(verbose_name="Image",upload_to="flowers_images")
    object_3d=models.FileField(verbose_name="3D Image",upload_to="flowers_obj",null=True,blank=True)
    price = models.FloatField(verbose_name="Price",default=0.0)
    special_price = models.FloatField(verbose_name="Promo Price",default=0.0)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
class Topic(models.Model):
    name=models.CharField(verbose_name="Name",max_length=200)
    name_ar=models.CharField(verbose_name="Arabic name",max_length=200)
    image=models.ImageField(verbose_name="Image",upload_to="topics_images")
    object_3d=models.FileField(verbose_name="3D Image",upload_to="topics_obj",null=True,blank=True)
    price = models.FloatField(verbose_name="Price",default=0.0)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
class Vase(models.Model):
    name=models.CharField(verbose_name="Name",max_length=200)
    name_ar=models.CharField(verbose_name="Arabic name",max_length=200)
    image=models.ImageField(verbose_name="Image",upload_to="vases_images")
    object_3d=models.FileField(verbose_name="3D Image",upload_to="vases_obj",null=True,blank=True)
    price = models.FloatField(verbose_name="Price",default=0.0)
    special_price = models.FloatField(verbose_name="Promo Price",default=0.0)
    max = models.PositiveIntegerField(verbose_name="max flowers",default=0)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    