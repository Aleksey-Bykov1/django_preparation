from django.db import models


class Product(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255)
    created_at = models.DateTimeField(verbose_name='Date_of-creation')
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=2, default=0)
    unit = models.CharField(verbose_name='Unit', max_length=8)
    vendor = models.CharField(verbose_name='Vendor', max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


