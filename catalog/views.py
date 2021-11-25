from django.shortcuts import render

from django.views.generic.list import ListView
from catalog.models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products_index.html'
    queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

    def get_queryset(self):
        qs = super(ProductListView, self).get_queryset()
        if category_id := self.kwargs.get('id'):
            qs = qs.filter(category_id=category_id)
        return qs
