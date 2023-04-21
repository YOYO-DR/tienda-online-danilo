from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200,  null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{str(self.user.id)} {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, )
    photo = models.ImageField(upload_to="products/%Y/%m", default=False)

    def __str__(self):
        return f'{self.id} {self.name}'


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False)
    cantidad = models.IntegerField(default=0)
    total=models.DecimalField(max_digits=12,decimal_places=1)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'
    class Meta:
        ordering = ['-product']
