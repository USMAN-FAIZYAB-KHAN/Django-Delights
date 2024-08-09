import datetime
from typing import Any
from django.shortcuts import render
from django.db.models import Sum

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm

def home(request):
    revenue = Purchase.objects.aggregate(Sum('total_price', default=0))['total_price__sum']
    cost = Purchase.objects.aggregate(Sum('total_cost_of_ingredients', default=0))['total_cost_of_ingredients__sum']
    profit = revenue - cost
    return render(request, 'inventory/home.html', {'revenue': revenue, 'cost': cost, 'profit': profit})


class IngredientListView(ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'
    context_object_name = 'ingredients'
    

class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_form.html'
    form_class = IngredientForm
    success_url = '/inventory/ingredients/'

class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = 'inventory/ingredient_form.html'
    form_class = IngredientForm
    success_url = '/inventory/ingredients/'

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'inventory/confirm_delete.html'
    success_url = '/inventory/ingredients/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url_name'] = 'ingredient_list'
        return context

class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'inventory/menuitem_list.html'
    context_object_name = 'menuitems'

class MenuItemCreateView(CreateView):
    model = MenuItem
    template_name = 'inventory/menuitem_form.html'
    form_class = MenuItemForm
    success_url = '/inventory/menuitems/'

class MenuItemUpdateView(UpdateView):
    model = MenuItem
    template_name = 'inventory/menuitem_form.html'
    form_class = MenuItemForm
    success_url = '/inventory/menuitems/'

class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = 'inventory/confirm_delete.html'
    success_url = '/inventory/menuitems/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url_name'] = 'menuitem_list'
        return context

class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = 'inventory/menuitem_detail.html'


class RecipeRequirementCreateView(CreateView):
    model = RecipeRequirement
    template_name = 'inventory/reciperequirement_form.html'
    form_class = RecipeRequirementForm
    success_url = '/inventory/reciperequirements/'

class RecipeRequirementUpdateView(UpdateView):
    model = RecipeRequirement
    template_name = 'inventory/reciperequirement_form.html'
    form_class = RecipeRequirementForm
    success_url = '/inventory/reciperequirements/'

class RecipeRequirementDeleteView(DeleteView):
    model = RecipeRequirement
    template_name = 'inventory/confirm_delete.html'
    success_url = '/inventory/reciperequirements/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_id'] = self.object.menu_item.id
        context['cancel_url_name'] = 'menuitem_detail'
        print(context)
        return context

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'inventory/purchase_list.html'
    context_object_name = 'purchases'

class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = 'inventory/purchase_form.html'
    form_class = PurchaseForm
    success_url = '/inventory/purchases/'

class PurchaseUpdateView(UpdateView):
    model = Purchase
    template_name = 'inventory/purchase_form.html'
    form_class = PurchaseForm
    success_url = '/inventory/purchases/'

class PurchaseDeleteView(DeleteView):
    model = Purchase
    template_name = 'inventory/confirm_delete.html'
    success_url = '/inventory/purchases/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url_name'] = 'purchase_list'
        return context