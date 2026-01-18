from django.contrib import admin
from .models import Product, CartItem, Order, OrderItem
from .models import Category
admin.site.register(Category)

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
