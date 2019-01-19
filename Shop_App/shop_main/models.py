from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length =100);
    last_name = models.CharField(max_length= 200);
    nick = models.CharField(max_length =100);
    password = models.CharField(max_length = 500);
    register_at = models.DateTimeField(default=datetime.now, blank=True);

    def __str__(self):
        return self.nick;
    class Meta:
        verbose_name_plural = 'User'

class Product_Type(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name;
    class Meta:
        verbose_name_plural = 'Product Type'

class Image(models.Model):
    name = models.CharField(max_length =100)
    img_source = models.CharField(max_length = 400)
    def __str__(self):
        return self.name;
    class Meta:
        verbose_name_plural = 'Image'

class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.DecimalField(decimal_places=2,max_digits=6)
    product_type = models.ForeignKey(Product_Type, related_name='Poroduct_type', on_delete=models.CASCADE);
    image = models.ForeignKey(Image,null=True, related_name='Image', on_delete=models.SET_NULL);
    amout = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name;
    class Meta:
        verbose_name_plural = 'Product'
