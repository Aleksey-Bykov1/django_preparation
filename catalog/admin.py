from django.contrib import admin

import catalog.models

admin.site.register(catalog.models.Category)
admin.site.register(catalog.models.Product)
