from django.db import models
from django.conf import settings


class Nutriment(models.Model):

    energy = models.fields.FloatField(null=False)
    protein = models.fields.FloatField(null=False)
    salt = models.fields.FloatField(null=False)
    sugar = models.fields.FloatField(null=False)
    saturedfat = models.fields.FloatField(null=False)
    fat = models.fields.FloatField(null=False)


class Product(models.Model):

    name = models.fields.CharField(max_length=150)
    categorie = models.fields.CharField(max_length=100)
    ecoscore = models.fields.CharField(max_length=1)
    image = models.fields.CharField(max_length=250)
    nutriment = models.ForeignKey(Nutriment, on_delete=models.CASCADE, null=True, related_name='nutriment')


class Favorite(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    base_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="base")
    substitute_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="substitute")
