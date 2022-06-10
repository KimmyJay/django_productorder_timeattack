from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = "category"
    name = models.CharField(max_length=70, default='')

class OrderStatus(models.Model):
    class Meta:
        db_table = "orderstatus"
    status = models.CharField(max_length=70, default='')
    payment = models.CharField(max_length=70, default='')
    cancel = models.CharField(max_length=70, default='')
    ship_start = models.CharField(max_length=70, default='')
    ship_complete = models.CharField(max_length=70, default='')

class ProductOrder(models.Model):
    class Meta:
        db_table = "productorder"
    product_count = models.PositiveIntegerField(default=0)

class Product(models.Model):
    class Meta:
        db_table = "product"
    name = models.CharField(max_length=70, default='')
    category = models.ManyToManyField(Category, related_name='product')
    description = models.TextField(max_length=256, default='')
    img = models.TextField(max_length=256, default='')
    inventory = models.PositiveIntegerField(default=0)
    product_order = models.ForeignKey(ProductOrder, on_delete=models.CASCADE)

class UserOrder(models.Model):
    class Meta:
        db_table = "userorder"
    product_order = models.ManyToManyField(ProductOrder, related_name='userorder')
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    delivery_address = models.TextField(max_length=256, default='')
    order_time = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.DecimalField(max_digits=1, decimal_places=2)
    valid = models.BooleanField(default=False)


