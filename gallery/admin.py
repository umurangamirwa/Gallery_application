# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Image,Category,Location
from django.contrib import admin

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)
admin.site.register(Location)
admin.site.register(Image)
admin.site.register(Category)
# Register your models here.
