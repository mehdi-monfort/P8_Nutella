from django.core.management.base import BaseCommand
from django.conf import settings
import requests
from ...models import Product, Nutriment


class Command(BaseCommand):
    args = '<team_id>'
    help = 'fill the openfoodfacts database'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.url = "https://world.openfoodfacts.org/cgi/search.pl?"

    def handle(self, *args, **options):

        for category in settings.CATEGORIES:
            params = {
                'action': 'process',
                'json': 1,
                'page_size': 500,
                'page': 1,
                'tagtype_0': 'categories',
                'tag_contains_0': 'contains',
                'tag_0': category,
            }
            response = requests.get(self.url, params=params)
            resp = response.json()

            for i in range(500):
                try:
                    prod = Product(
                        resp["products"][i].get("categories", "0"),
                        resp["products"][i].get("product_name_fr", "0"),
                        resp["products"][i].get("ecoscore_grade", "unknown"),
                        resp["products"][i].get("image_front_url", "0"),
                    )
                    nut = Nutriment(
                        resp["products"][i]["nutriscore_data"].get("proteins", "0"),
                        resp["products"][i]["nutriscore_data"].get("sodium", "0"),
                        resp["products"][i]["nutriscore_data"].get("sugars", "0"),
                        resp["products"][i]["nutriscore_data"].get("satured_fat", "0"),
                    )
                    checkers = [
                        prod.ecoscore != "0" and
                        prod.categorie != "unknown"
                    ]
                    if all(checkers):

                        Nutriment.objects.create(
                            protein=nut.protein,
                            salt=nut.salt,
                            sugar=nut.sugar,
                            fat=nut.fat,
                        )
                        Product.objects.create(
                            name=prod.name,
                            categorie=category,
                            ecoscore=prod.categorie,
                            image=prod.ecoscore,
                        )

                    else:
                        continue

                except KeyError:
                    continue

                except IndexError:
                    continue
