from django.contrib import admin
from .models import (
    Category, Dish, Ingredient, Menu, Allergen,
    Customer, Order, OrderItem, Chef, Tag
)

# Inline display of order items within an order
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'created_at')
    inlines = [OrderItemInline]


# Register all models for admin interface
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(Menu)
admin.site.register(Allergen)
admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(Chef)
admin.site.register(Tag)
