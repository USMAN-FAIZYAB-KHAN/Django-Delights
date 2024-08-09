from django.db import transaction
from typing import Any
from django.shortcuts import render
from django.db.models import Sum
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm, CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

@login_required
def home(request):
    revenue = Purchase.objects.aggregate(Sum('total_price', default=0))['total_price__sum']
    cost = Purchase.objects.aggregate(Sum('total_cost_of_ingredients', default=0))['total_cost_of_ingredients__sum']
    profit = revenue - cost
    return render(request, 'inventory/home.html', {'revenue': revenue, 'cost': cost, 'profit': profit})


class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'
    context_object_name = 'ingredients'
    

class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = 'inventory/create_form.html'
    form_class = IngredientForm
    success_url = '/inventory/ingredients/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Ingredient'
        return context

class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = 'inventory/update_form.html'
    form_class = IngredientForm
    success_url = '/inventory/ingredients/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Ingredient'
        return context

class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = 'inventory/confirm_delete.html'
    success_url = '/inventory/ingredients/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url_name'] = 'ingredient_list'
        return context

class MenuItemListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = 'inventory/menuitem_list.html'
    context_object_name = 'menuitems'

class MenuItemCreateView(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = 'inventory/create_form.html'
    form_class = MenuItemForm
    success_url = '/inventory/menuitems/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Menu Item'

class MenuItemUpdateView(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = 'inventory/update_form.html'
    form_class = MenuItemForm
    success_url = '/inventory/menuitems/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Menu Item'
        return context

class MenuItemDeleteView(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = 'inventory/confirm_delete.html'
    success_url = '/inventory/menuitems/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url_name'] = 'menuitem_list'
        return context

class MenuItemDetailView(LoginRequiredMixin, DetailView):
    model = MenuItem
    template_name = 'inventory/menuitem_detail.html'

    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context["items_sold"] = Purchase.objects.filter(menu_item=self.object).count()
        return context


class RecipeRequirementCreateView(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = 'inventory/create_form.html'
    form_class = RecipeRequirementForm
    success_url = '/inventory/reciperequirements/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Recipe Requirement'
        return context

class RecipeRequirementUpdateView(LoginRequiredMixin, UpdateView):
    model = RecipeRequirement
    template_name = 'inventory/update_form.html'
    form_class = RecipeRequirementForm
    success_url = '/inventory/reciperequirements/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Recipe Requirement'
        return context

class RecipeRequirementDeleteView(LoginRequiredMixin, DeleteView):
    model = RecipeRequirement
    template_name = 'inventory/confirm_delete.html'
    success_url = '/inventory/reciperequirements/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_id'] = self.object.menu_item.id
        context['cancel_url_name'] = 'menuitem_detail'
        print(context)
        return context

class PurchaseListView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'inventory/purchase_list.html'
    context_object_name = 'purchases'

class PurchaseCreateView(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = 'inventory/create_form.html'
    form_class = PurchaseForm
    success_url = '/inventory/purchases/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Purchase'
        return context
    
    @transaction.atomic
    def form_valid(self, form):
        menu_item = form.cleaned_data['menu_item']
        item_count = form.cleaned_data['quantity']

        insufficent_quantity = False

        # Check if there is sufficient quantity of each ingredient
        for req in menu_item.reciperequirement_set.all():
            ingredient = req.ingredient
            required_quantity = req.quantity * item_count
            if ingredient.quantity < required_quantity:
                # Add an error if not enough quantity is available
                insufficent_quantity = True
                form.add_error(None, f"Insufficient quantity of {ingredient.name}")

        if insufficent_quantity:   
            return super().form_invalid(form)

        # If all checks pass, update the ingredient quantities
        for req in menu_item.reciperequirement_set.all():
            ingredient = req.ingredient
            required_quantity = req.quantity * item_count
            ingredient.quantity -= required_quantity
            ingredient.save()

        # Proceed with saving the purchase
        return super().form_valid(form)
    

class PurchaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Purchase
    template_name = 'inventory/update_form.html'
    form_class = PurchaseForm
    success_url = '/inventory/purchases/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Purchase'
        return context

class PurchaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = 'inventory/confirm_delete.html'
    success_url = '/inventory/purchases/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url_name'] = 'purchase_list'
        return context