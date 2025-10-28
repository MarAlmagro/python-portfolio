from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import (
    Dish, Menu, Category, Ingredient,
    Tag, Chef
)

LIST_TEMPLATE = 'delights/list.html'
DETAIL_TEMPLATE = 'delights/detail.html'
DELETE_TEMPLATE = 'delights/confirm_delete.html'

class BaseDetailView(DetailView):
    """Base detail view that excludes the ID field and sets a dynamic title."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.object

        # Exclude the object's ID field so it doesn't appear in the template
        fields = [
            (field.verbose_name, getattr(obj, field.name))
            for field in obj._meta.fields
            if field.name != "id"
        ]

        context["fields"] = fields
        context["title"] = f"{obj._meta.verbose_name.title()}: {obj}"
        return context


# ----------- Dish Views -----------

class DishListView(ListView):
    model = Dish
    template_name = LIST_TEMPLATE
    extra_context = {'title': 'Dishes'}

class DishDetailView(BaseDetailView):
    model = Dish
    template_name = DETAIL_TEMPLATE
    
class DishCreateView(CreateView):
    model = Dish
    fields = '__all__'
    template_name = 'dish_form.html'
    success_url = reverse_lazy('dish_list')

class DishUpdateView(UpdateView):
    model = Dish
    fields = '__all__'
    template_name = 'dish_form.html'
    success_url = reverse_lazy('dish_list')

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

class MenuCreateView(CreateView):
    model = Menu
    fields = '__all__'
    template_name = 'menu_form.html'
    success_url = reverse_lazy('menu_list')

class MenuUpdateView(UpdateView):
    model = Menu
    fields = '__all__'
    template_name = 'menu_form.html'
    success_url = reverse_lazy('menu_list')

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

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

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

class IngredientCreateView(CreateView):
    model = Ingredient
    fields = '__all__'
    template_name = 'ingredient_form.html'
    success_url = reverse_lazy('ingredient_list')

class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = '__all__'
    template_name = 'ingredient_form.html'
    success_url = reverse_lazy('ingredient_list')

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

class TagCreateView(CreateView):
    model = Tag
    fields = '__all__'
    template_name = 'tag_form.html'
    success_url = reverse_lazy('tag_list')

class TagUpdateView(UpdateView):
    model = Tag
    fields = '__all__'
    template_name = 'tag_form.html'
    success_url = reverse_lazy('tag_list')

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

class ChefCreateView(CreateView):
    model = Chef
    fields = '__all__'
    template_name = 'chef_form.html'
    success_url = reverse_lazy('chef_list')

class ChefUpdateView(UpdateView):
    model = Chef
    fields = '__all__'
    template_name = 'chef_form.html'
    success_url = reverse_lazy('chef_list')

class ChefDeleteView(DeleteView):
    model = Chef
    template_name = DELETE_TEMPLATE
    success_url = reverse_lazy('chef_list')
