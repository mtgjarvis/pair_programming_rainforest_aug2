from django.db import models
from django.forms import ModelForm


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.description} {self.price}"


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price"]

