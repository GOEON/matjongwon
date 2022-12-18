from django.core.management.base import BaseCommand, CommandError
from v1.models import Place
import json
import os

class Command(BaseCommand):
    help = 'Load the JSON data and insert it to Place DB'

    DATA_FILE_PATH = os.path.join('../..', 'scrapers', 'data', 'final_contents.json')

    def add_argument(self, parser):
        parser.add_argument(
            '-f',
            '--file',
            action='store',
            help='JSON data file location',
        )


    def handle(self, *args, **options):
        json_file = self.DATA_FILE_PATH

        option_file = options.get('file')
        if option_file:
            if os.path.exists(option_file) and os.path.isfile(option_file):
                json_file = option_file

        with open(json_file, 'r') as f:
            data = json.load(f)
            objects = []
            for place in data:
                objects.append(self._import_place(place))
            Place.objects.bulk_create(objects)

            self.stdout.write(self.style.SUCCESS('Successfully added json data'))

    def _import_place(self, place_data):
        place = Place(
            name = place_data['name'],
            category = place_data['category'],
            address = place_data['address'],
            opening_hours = place_data['opening_hours'],
            score = place_data['score'],
            menu = place_data['menu'],
            url = place_data['url'],
            reviews = place_data['reviews'],
            thumbnails = place_data['thumbnails'],
            description = place_data['description'],
            coordinates = place_data['coordinates'],
        )
        return place
