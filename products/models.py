from django.db import models

class product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    img_url = models.CharField(max_length=2083)

class Offer(models.Model):
    code = models.CharField(max_length=30)
    description = models.CharField(max_length=2083)    
    discount = models.FloatField()

class Image(models.Model):
    photo = models.ImageField(upload_to="gallery")
