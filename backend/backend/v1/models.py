from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)
    # TOO: add category -> use plain json encoding
    category = models.JSONField()
    address = models.CharField(max_length=200)
    opening_hours = models.CharField(max_length=200)
    # TODO: add score -> work around: use separte score for each site
    kakao_score = models.DecimalField(max_digits=2, decimal_places=1)
    tripadvisor_score = models.DecimalField(max_digits=2, decimal_places=1)
    google_score = models.DecimalField(max_digits=2, decimal_places=1)
    # TODO: add menu -> use plain json encoding
    menu = models.JSONField()
    place_url = models.URLField(max_length=200)
    review_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name
