# -*- coding: utf-8 -*-
from django.db import models
class Category(models.Model):
        name = models.CharField(max_length =30)

        def __str__(self):
            return self.name

        def save_category(self):
            self.save()

        @classmethod
        def delete_category(cls,name):
            cls.objects.filter(name = name).delete()

        
        def update_category(self, **kwargs):
            self.objects.filter(id = self.pk).update(**kwargs)

class Location(models.Model):
        name = models.CharField(max_length=20)

        def __str__(self):
            return self.name

        def save_location(self):
            self.save()
        @classmethod  
        def delete_location(cls,name):
            cls.objects.filter(name = name).delete()
            
    
        def update_location(self, **kwargs):
            self.objects.filter(id = self.pk).update(**kwargs)

class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/', null = True)
    name = models.CharField(max_length =30)
    description = models.CharField(max_length=100)
    location = models.ForeignKey(Location,on_delete = models.CASCADE)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    
    
    def save_image(self):
        self.save()

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete()
    
    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)

    @classmethod
    def all_pictures(cls):
        pictures = cls.objects.all()
        return pictures

    @classmethod
    def pic_locations(cls):
        pictures = cls.objects.order_by('location')
        return pictures

    @classmethod
    def pic_categories(cls):
        pictures = cls.objects.order_by('category')
        return pictures

    

    @classmethod
    def get_pic(cls, id):
        picture = cls.objects.get(id=id)
        return picture

    @classmethod
    def search_by_category(cls, search_input):
        images = cls.objects.filter(category__name__icontains=search_input)
        return images

     
