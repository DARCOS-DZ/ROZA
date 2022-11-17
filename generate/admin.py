from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Flower)
admin.site.register(Vase)
admin.site.register(Topic)
admin.site.register(Position)
admin.site.register(Category)