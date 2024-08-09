from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # URL patterns for Ingredient
    path("ingredients/", views.IngredientListView.as_view(), name="ingredient_list"),
    path("ingredients/create/", views.IngredientCreateView.as_view(), name="ingredient_create"),
    path("ingredients/update/<int:pk>/", views.IngredientUpdateView.as_view(), name="ingredient_update"),
    path("ingredients/delete/<int:pk>/", views.IngredientDeleteView.as_view(), name="ingredient_delete"),
    # URL patterns for MenuItem
    path("menuitems/", views.MenuItemListView.as_view(), name="menuitem_list"),
    path("menuitems/create/", views.MenuItemCreateView.as_view(), name="menuitem_create"),
    path("menuitems/update/<int:pk>/", views.MenuItemUpdateView.as_view(), name="menuitem_update"),
    path("menuitems/delete/<int:pk>/", views.MenuItemDeleteView.as_view(), name="menuitem_delete"),
    path("menuitems/<int:pk>/", views.MenuItemDetailView.as_view(), name="menuitem_detail"),
    # URL patterns for RecipeRequirement
    path("reciperequirements/create/", views.RecipeRequirementCreateView.as_view(), name="reciperequirement_create"),
    path("reciperequirements/update/<int:pk>/", views.RecipeRequirementUpdateView.as_view(), name="reciperequirement_update"),
    path("reciperequirements/delete/<int:pk>/", views.RecipeRequirementDeleteView.as_view(), name="reciperequirement_delete"),
    # URL patterns for Purchase
    path("purchases/", views.PurchaseListView.as_view(), name="purchase_list"),
    path("purchases/create/", views.PurchaseCreateView.as_view(), name="purchase_create"),
    path("purchases/update/<int:pk>/", views.PurchaseUpdateView.as_view(), name="purchase_update"),
    path("purchases/delete/<int:pk>/", views.PurchaseDeleteView.as_view(), name="purchase_delete"),
]