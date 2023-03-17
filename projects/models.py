from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # image = models.FilePathField(path="/img")
    image=models.CharField(max_length=100)

class Cart(models.Model):
    # one to one relation to Product
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()