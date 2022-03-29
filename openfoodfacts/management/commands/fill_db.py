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
                'search_simple': 1,
                'search_terms': category,
            }
            response = requests.get(self.url, params=params)
            resp = response.json()
            for i in range(500):
                prod = Product(
                    name=resp["products"][i].get("product_name_fr", ""),
                    ecoscore=resp["products"][i].get("ecoscore_grade", "unknown"),
                    image=resp["products"][i].get("image_front_url", "0")
                )
                nut = Nutriment(
                    energy=resp["products"][i]["nutriments"].get("energy_100g", "e"),
                    protein=resp["products"][i]["nutriments"].get("proteins_100g", "e"),
                    salt=resp["products"][i]["nutriments"].get("sodium_100g", "e"),
                    sugar=resp["products"][i]["nutriments"].get("sugars_100g", "e"),
                    fat=resp["products"][i]["nutriments"].get("saturated-fat_100g", "e")
                )
                checkers = [
                    prod.ecoscore != "unknown" and
                    prod.ecoscore != "not-applicable" and
                    prod.name != "" and nut.salt != "e" and
                    prod.image != "0" and nut.sugar != "e" and
                    nut.energy != "e" and nut.fat != "e" and
                    nut.fat != "e"
                    ]
                if all(checkers):

                    Nutriment.objects.create(
                        energy=nut.energy,
                        protein=nut.protein,
                        salt=nut.salt,
                        sugar=nut.sugar,
                        fat=nut.fat,
                    )

                    Product.objects.create(
                        categorie=category,
                        name=prod.name,
                        ecoscore=prod.ecoscore.upper(),
                        image=prod.image,
                    )

                else:
                    continue
