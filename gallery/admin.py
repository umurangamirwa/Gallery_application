# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Editor,Article,tags
from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)
# Register your models here.
