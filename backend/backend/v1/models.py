from django.db import models
import json

class Place(models.Model):
    name = models.CharField(max_length=200)
    category = models.JSONField()
    address = models.CharField(max_length=200)
    opening_hours = models.JSONField()
    score = models.JSONField() # Use JsonField for dictionary type
    # kakao_score = models.DecimalField(max_digits=2, decimal_places=1)
    # tripadvisor_score = models.DecimalField(max_digits=2, decimal_places=1)
    # google_score = models.DecimalField(max_digits=2, decimal_places=1)
    menu = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    reviews = models.JSONField()
    thumbnails = models.JSONField()
    description = models.CharField(max_length=300)
    coordinates = models.JSONField(default=dict)

    def __str__(self):
        return self.name
