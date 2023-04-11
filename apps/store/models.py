from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False,verbose_name='Usuario')
    name = models.CharField(max_length=200,null=False,blank=False,verbose_name='Nombre')
    email = models.EmailField(max_length=200,null=False,blank=False,verbose_name='Email')

    class Meta:
      verbose_name='Cliente'
      verbose_name_plural='Clientes'
      db_table = 'customers'

class Order(models.Model):
  trasnsation_id = models.AutoField(primary_key=True)
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=False,blank=False,verbose_name='Cliente')
  data_ordered = models.DateTimeField(auto_now_add=True)
  complete = models.BooleanField(default=False)

  class Meta:
   db_table = 'orders'
   verbose_name = 'Pedido'
   verbose_name_plural = 'Pedidos'

class ShippingAddress(models.Model):
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
  order = models.ForeignKey(Order,on_delete=models.CASCADE)
  address = models.CharField(max_length=200,null=True,blank=False,verbose_name='Dirección')
  city = models.CharField(max_length=200,null=True,blank=False,verbose_name='Ciudad')
  state = models.CharField(max_length=200,null=True,blank=False,verbose_name='Estado')
  zipcode = models.IntegerField(null=True,blank=False,verbose_name='Codigo Postal')
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
   db_table = 'address'
   verbose_name = 'Dirección'
   verbose_name_plural = 'Direcciones'

class Product(models.Model):
  name = models.CharField(max_length=200,null=False,blank=False,verbose_name='Producto')
  price = models.DecimalField(max_digits=9,decimal_places=2,null=False,blank=False,verbose_name='Precop')
  digital = models.BooleanField(default=False)
  #se necesita pillow para la imagen
  image = models.ImageField(upload_to='images/%Y/%m/%d',null=False,blank=False,verbose_name='Imagen del producto')

  class Meta:
   db_table = 'product'
   verbose_name = 'Producto'
   verbose_name_plural = 'Productos'

class OrderItem(models.Model):
  product = models.ForeignKey(Product,on_delete=models.CASCADE,null=False,blank=False,verbose_name='Producto')
  order = models.ForeignKey(Order,on_delete=models.CASCADE,null=False,blank=False,verbose_name='Pedido')
  quanitity = models.IntegerField(null=False,blank=False,verbose_name='Cantidad')
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
   db_table = 'orderitems'
   verbose_name = 'Articulo pedido'
   verbose_name_plural = 'Articulos pedidos'