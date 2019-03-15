# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime as dt

class Image(models.Model):
    image = models.CharField(max_length =30)
    name = models.CharField(max_length =30)
    description = models.EmailField()
    location = models.CharField('Location', on_delete = models.CASCADE, null='True',blank =True)
    category = models.CharField('Category', on_delete = models.CASCADE, null='True',blank =True)
    def __str__(self):
        return self.first_name
    def save_image(self):
        self.save()

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete()
    
    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)

        
class Meta:
        ordering = ['first_name']

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
class Category(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete = models.CASCADE )  
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def todays_gallery(cls):
        today = dt.date.today()
        garelly = cls.objects.filter(pub_date__date = today)
        return gallery
# Create your models here.
