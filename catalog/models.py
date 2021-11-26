from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=64, unique=True)
    description = models.TextField(verbose_name='Description', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(verbose_name='Title', max_length=255)
    created_at = models.DateTimeField(verbose_name='Date_of-creation')
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=2, default=0)
    unit = models.CharField(verbose_name='Unit', max_length=8)
    vendor = models.CharField(verbose_name='Vendor', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
