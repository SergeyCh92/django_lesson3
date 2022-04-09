import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for el in phones:
            data = Phone(
                id=el['id'],
                name=el['name'],
                image=el['image'],
                price=el['price'],
                release_date=el['release_date'],
                lte_exists=el['lte_exists'],
                slug=el['name'].lower().replace(' ', '-')
            )
            data.save()

        for phone in phones:
            # TODO: Добавьте сохранение модели
            pass
