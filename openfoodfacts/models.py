from django.db import models
from django.conf import settings


class Nutriment(models.Model):

    protein = models.fields.FloatField(null=True)
    salt = models.fields.FloatField(null=True)
    sugar = models.fields.FloatField(null=True)
    fat = models.fields.FloatField(null=True)


class Product(models.Model):

    name = models.fields.CharField(max_length=150)
    categorie = models.fields.CharField(max_length=100)
    ecoscore = models.fields.CharField(max_length=1)
    image = models.fields.CharField(max_length=250)
    nutriment = models.OneToOneField(Nutriment, on_delete=models.CASCADE, null=True, related_name='nutriment')


class Favorite(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    base_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="base")
    substitute_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="substitute")
