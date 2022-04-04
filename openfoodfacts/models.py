from django.db import models
from django.conf import settings


class Product(models.Model):

    name = models.fields.CharField(max_length=150)
    categorie = models.fields.CharField(max_length=100)
    ecoscore = models.fields.CharField(max_length=1)
    image = models.fields.CharField(max_length=250)
    linkoff = models.fields.CharField(max_length=250)


class Nutriment(models.Model):

    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    energy = models.fields.FloatField(null=False)
    protein = models.fields.FloatField(null=False)
    salt = models.fields.FloatField(null=False)
    sugar = models.fields.FloatField(null=False)
    saturedfat = models.fields.FloatField(null=False)
    fat = models.fields.FloatField(null=False)


class Favorite(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    substitute = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="substitute")
