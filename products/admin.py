from django.contrib import admin
from .models import product, Offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(product, ProductAdmin)

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')

admin.site.register(Offer, OfferAdmin)