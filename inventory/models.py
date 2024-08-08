from django.db import models
import datetime

# Create your models here.
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
    unit = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.menu_item.title} - {self.ingredient.name} - {self.quantity} {self.unit}"
    
    class Meta:
        unique_together = ('menu_item', 'ingredient')

class Purchase(models.Model):
    """It represents a purchase made by a customer"""
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unit_price = models.FloatField(default=0.0)
    total_price = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.menu_item.title} - {self.quantity} - {self.timestamp}"
    
    class Meta:
        ordering = ['-timestamp']
