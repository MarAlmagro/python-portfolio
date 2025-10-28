from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import (
    Dish, Menu, Category, Ingredient,
    Tag, Chef
)

LIST_TEMPLATE = 'list.html'

# ----------- Dish Views -----------

class DishListView(ListView):
    model = Dish
    template_name = LIST_TEMPLATE
    extra_context = {'title': 'Dishes'}

class DishDetailView(DetailView):
    model = Dish
    template_name = 'dish_detail.html'

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
    template_name = 'dish_confirm_delete.html'
    success_url = reverse_lazy('dish_list')


# ----------- Menu Views -----------

class MenuListView(ListView):
    model = Menu
    template_name = LIST_TEMPLATE
    extra_context = {'title': 'Menus'}

class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu_detail.html'

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
    template_name = 'menu_confirm_delete.html'
    success_url = reverse_lazy('menu_list')


# ----------- Category Views -----------

class CategoryListView(ListView):
    model = Category
    template_name = LIST_TEMPLATE
    extra_context = {'title': 'Categories'}

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'

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
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category_list')


# ----------- Ingredient Views -----------

class IngredientListView(ListView):
    model = Ingredient
    template_name = LIST_TEMPLATE
    extra_context = {'title': 'Ingredients'}

class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'ingredient_detail.html'

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
    template_name = 'ingredient_confirm_delete.html'
    success_url = reverse_lazy('ingredient_list')


# ----------- Tag Views -----------

class TagListView(ListView):
    model = Tag
    template_name = LIST_TEMPLATE
    extra_context = {'title': 'Tags'}

class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag_detail.html'

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
    template_name = 'tag_confirm_delete.html'
    success_url = reverse_lazy('tag_list')


# ----------- Chef Views -----------

class ChefListView(ListView):
    model = Chef
    template_name = LIST_TEMPLATE
    extra_context = {'title': 'Chefs'}

class ChefDetailView(DetailView):
    model = Chef
    template_name = 'chef_detail.html'

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
    template_name = 'chef_confirm_delete.html'
    success_url = reverse_lazy('chef_list')
