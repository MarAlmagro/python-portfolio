from django.db import models


# Categorizes dishes (e.g., starter, main course, dessert)
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Chef who can prepare one or more dishes
class Chef(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Additional classification for dishes (e.g., vegan, spicy)
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Ingredient used in dishes
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Allergen linked to one or more ingredients
class Allergen(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, related_name='allergens')

    def __str__(self):
        return self.name


# Represents a dish or recipe
class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    ingredients = models.ManyToManyField(Ingredient, related_name='dishes')
    tags = models.ManyToManyField(Tag, blank=True, related_name='dishes')
    chefs = models.ManyToManyField(Chef, blank=True, related_name='dishes')

    def __str__(self):
        return self.name


# Collection of dishes (e.g., daily menu)
class Menu(models.Model):
    name = models.CharField(max_length=100)
    dishes = models.ManyToManyField(Dish, related_name='menus')

    def __str__(self):
        return self.name


# Customer who places an order
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


# Order placed by a customer
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.name}"


# Single line item within an order
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.dish.name}"
