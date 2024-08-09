from django.db import models
import datetime

class Ingredient(models.Model):
    """It represents a single ingredient in the restaurant's inventory"""
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=100)
    unit_price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    """It represents an entry off the restaurant's menu"""
    title = models.CharField(max_length=100, unique=True)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class RecipeRequirement(models.Model):
    """It represents an ingredient required for a recipe for a MenuItem"""
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)

    def __str__(self):
        return self.ingredient.name
    
    class Meta:
        unique_together = ('menu_item', 'ingredient')

class Purchase(models.Model):
    """It represents a purchase made by a customer"""
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_cost_of_ingredients = models.FloatField(default=0.0)
    # The price at which the menu item is sold to the customer
    unit_price = models.FloatField(default=0.0)
    # The total price of the menu item sold to the customer
    total_price = models.FloatField(default=0.0)

    def calculate_total_cost_of_ingredients(self):
        """It calculates the total cost of the ingredients required to make the menu item at the time of purchase"""
        total_cost = 0
        for req in self.menu_item.reciperequirement_set.all():
            total_cost += req.ingredient.unit_price * req.quantity
        return total_cost
    
    def save(self, *args, **kwargs):
        self.total_cost_of_ingredients = self.calculate_total_cost_of_ingredients()
        self.unit_price = self.menu_item.price
        self.total_price = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.menu_item.title} - {self.quantity} - {self.timestamp}"
    
    class Meta:
        ordering = ['-timestamp']
