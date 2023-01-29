from django.db import models


class Place(models.Model):
    name = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    opening_hours = models.TextField(blank=True, null=True)
    score_navermap = models.TextField(db_column='score.navermap', blank=True, null=True)
    score_kakaomap = models.TextField(db_column='score.kakaomap', blank=True, null=True)
    score_googlemap = models.TextField(db_column='score.googlemap', blank=True, null=True)
    menu = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    reviews_navermap = models.TextField(db_column='reviews.navermap', blank=True, null=True)
    reviews_kakaomap = models.TextField(db_column='reviews.kakaomap', blank=True, null=True)
    reviews_googlemap = models.TextField(db_column='reviews.googlemap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    thumbnails = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    coordinates_latitude = models.TextField(db_column='coordinates.latitude', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    coordinates_longitude = models.TextField(db_column='coordinates.longitude', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'gangnam'
    
    def __str__(self):
        return self.name
