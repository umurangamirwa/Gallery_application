# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Editor,Article,tags
from django.contrib import admin

admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tags)
# Register your models here.
