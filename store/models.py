from django.db import models
from django.contrib.auth.models import User
from config.settings import MEDIA_URL, STATIC_URL

class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200,  null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{str(self.id)} {self.name}'
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class CategoryProduct(models.Model):
    name = models.CharField(max_length=100,verbose_name='Nombre')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, )
    #para que se guarde en azure en la carpeta media, igual debe estar el media_url como '/media/' para concatenarlo en el get_photo
    photo = models.ImageField(upload_to="media/products/%Y/%m", null=True, blank=True)
    category=models.ForeignKey(CategoryProduct, on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self):
        return f'{self.id} {self.name}'
    
    def get_photo(self):
        if self.photo: #si tiene foto, la paso con la media url porque es un link externo, de lo contrario, una imagen de que no esta
            return f'{MEDIA_URL}{self.photo}'
        return f'{STATIC_URL}images/empty.png'
          
    
    # def save(self, *args, **kwargs):
    #     if self.photo:
    #       subirAzureBlobs(self,tipo_a='image') # Función para subir las fotos a azure blobs storage
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Cart(models.Model):
    user = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.name}'
    
    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'

class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False)
    cantidad = models.IntegerField(default=0)

    def total(self): #en vez de guardar el valor, mejor lo genero
        return self.cantidad*self.product.price

    def __str__(self):
        return f'{self.cantidad} / {self.product.name} - {self.cart.user.name}'
    
    class Meta:
        verbose_name = 'Item carrito'
        verbose_name_plural = 'Items carrito'