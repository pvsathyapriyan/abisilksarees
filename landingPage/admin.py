from django.contrib import admin

from .models import Product, Account, UPI

admin.site.register(Product)
admin.site.register(Account)
admin.site.register(UPI)
