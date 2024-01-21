from django.contrib import admin
from .models import demo
# Register your models here.
class demo_reg(admin.ModelAdmin):
    list_display=['id','name']
    
admin.site.register(demo,demo_reg)