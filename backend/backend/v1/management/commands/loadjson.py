from django.core.management.base import BaseCommand, CommandError
from v1.models import Place
import json
import os

class Command(BaseCommand):
    help = 'Load the JSON data and insert it to Place DB'

    def handle(self, *args, **options):
        json_path = os.path.join('../..', 'scrapers', 'data', 'final_contents.json')
        with open(json_path) as f:
            data = json.load(f)
            objects = []
            for i, entry in enumerate(data):
                obj = Place(
                    name = entry['name'],
                    category = entry['category'],
                    address = entry['address'],
                    opening_hours = entry['opening_hours'],
                    score = entry['score'],
                    menu = entry['menu'],
                    url = entry['url'],
                    reviews = entry['reviews'],
                    thumbnails = entry['thumbnails'],
                    description = entry['description'],
                    coordinates = entry['coordinates'],
                )
                objects.append(obj)
            Place.objects.bulk_create(objects)

            self.stdout.write(self.style.SUCCESS('Successfully added json data'))
