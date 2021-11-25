from django.shortcuts import render

from django.views.generic.list import ListView
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products_index.html'
    queryset = Product.objects.all()
