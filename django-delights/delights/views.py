from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import (
    Dish, Menu, Category, Ingredient,
    Tag, Chef
)
from django.contrib import messages

LIST_TEMPLATE = 'delights/list.html'
DETAIL_TEMPLATE = 'delights/detail.html'
DELETE_TEMPLATE = 'delights/confirm_delete.html'

class BaseDetailView(DetailView):
    """Base detail view that excludes the ID field and sets a dynamic title."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Exclude the object's ID field so it doesn't appear in the template
        fields = [
            (field.verbose_name, getattr(self.object, field.name))
            for field in self.object._meta.fields
            if field.name != "id"
        ]

        context["fields"] = fields
        context["title"] = f"{self.object._meta.verbose_name.title()}: {self.object}"
        return context

class BaseFormView:
    """Common logic for Create and Update views, excluding the ID field."""

    template_name = "delights/form.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        action = "Update" if isinstance(self, UpdateView) else "Create"
        model_name = self.model._meta.verbose_name.title()
        context["title"] = f"{action} {model_name}"
        return context

    def get_form(self, form_class=None):
        """Remove the ID field from the form before rendering."""
        form = super().get_form(form_class)
        form.fields.pop("id", None)
        return form
    
    def form_valid(self, form):
        """Add success message when form is successfully submitted."""
        response = super().form_valid(form)
        action = "updated" if isinstance(self, UpdateView) else "created"
        messages.success(self.request, f"{self.model._meta.verbose_name.title()} {action} successfully!")
        return response
    
    def get_success_url(self):
        """Redirect to the detail page of the created or updated object."""
        return self.object.get_absolute_url()

# ----------- Dish Views -----------

class DishListView(ListView):
    model = Dish
    template_name = LIST_TEMPLATE
    extra_context = {'title': 'Dishes'}

class DishDetailView(BaseDetailView):
    model = Dish
    template_name = DETAIL_TEMPLATE
    
class DishCreateView(BaseFormView, CreateView):
    model = Dish

class DishUpdateView(BaseFormView, UpdateView):
    model = Dish

class DishDeleteView(DeleteView):
    model = Dish
    template_name = DELETE_TEMPLATE
    success_url = reverse_lazy('dish_list')


# ----------- Menu Views -----------

class MenuListView(ListView):
    model = Menu
    template_name = LIST_TEMPLATE
    extra_context = {'title': 'Menus'}

class MenuDetailView(BaseDetailView):
    model = Menu
    template_name = DETAIL_TEMPLATE

class MenuCreateView(BaseFormView, CreateView):
    model = Menu

class MenuUpdateView(BaseFormView, UpdateView):
    model = Menu

class MenuDeleteView(DeleteView):
    model = Menu
    template_name = DELETE_TEMPLATE
    success_url = reverse_lazy('menu_list')


# ----------- Category Views -----------

class CategoryListView(ListView):
    model = Category
    template_name = LIST_TEMPLATE
    extra_context = {'title': 'Categories'}

class CategoryDetailView(BaseDetailView):
    model = Category
    template_name = DETAIL_TEMPLATE

class CategoryCreateView(BaseFormView, CreateView):
    model = Category

class CategoryUpdateView(BaseFormView, UpdateView):
    model = Category

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = DELETE_TEMPLATE
    success_url = reverse_lazy('category_list')


# ----------- Ingredient Views -----------

class IngredientListView(ListView):
    model = Ingredient
    template_name = LIST_TEMPLATE
    extra_context = {'title': 'Ingredients'}

class IngredientDetailView(BaseDetailView):
    model = Ingredient
    template_name = DETAIL_TEMPLATE

class IngredientCreateView(BaseFormView, CreateView):
    model = Ingredient

class IngredientUpdateView(BaseFormView, UpdateView):
    model = Ingredient

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = DELETE_TEMPLATE
    success_url = reverse_lazy('ingredient_list')


# ----------- Tag Views -----------

class TagListView(ListView):
    model = Tag
    template_name = LIST_TEMPLATE
    extra_context = {'title': 'Tags'}

class TagDetailView(BaseDetailView):
    model = Tag
    template_name = DETAIL_TEMPLATE

class TagCreateView(BaseFormView, CreateView):
    model = Tag

class TagUpdateView(BaseFormView, UpdateView):
    model = Tag

class TagDeleteView(DeleteView):
    model = Tag
    template_name = DELETE_TEMPLATE
    success_url = reverse_lazy('tag_list')


# ----------- Chef Views -----------

class ChefListView(ListView):
    model = Chef
    template_name = LIST_TEMPLATE
    extra_context = {'title': 'Chefs'}

class ChefDetailView(BaseDetailView):
    model = Chef
    template_name = DETAIL_TEMPLATE

class ChefCreateView(BaseFormView, CreateView):
    model = Chef

class ChefUpdateView(BaseFormView, UpdateView):
    model = Chef

class ChefDeleteView(DeleteView):
    model = Chef
    template_name = DELETE_TEMPLATE
    success_url = reverse_lazy('chef_list')
