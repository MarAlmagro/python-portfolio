from django.urls import path
from .views import (
    # Dish views
    DishListView, DishDetailView, DishCreateView,
    DishUpdateView, DishDeleteView,

    # Menu views
    MenuListView, MenuDetailView, MenuCreateView,
    MenuUpdateView, MenuDeleteView,

    # Category views
    CategoryListView, CategoryDetailView, CategoryCreateView,
    CategoryUpdateView, CategoryDeleteView,

    # Ingredient views
    IngredientListView, IngredientDetailView, IngredientCreateView,
    IngredientUpdateView, IngredientDeleteView,

    # Tag views
    TagListView, TagDetailView, TagCreateView,
    TagUpdateView, TagDeleteView,

    # Chef views
    ChefListView, ChefDetailView, ChefCreateView,
    ChefUpdateView, ChefDeleteView,
)


urlpatterns = [
    # Dish
    path('dishes/', DishListView.as_view(), name='dish_list'),
    path('dishes/<int:pk>/', DishDetailView.as_view(), name='dish_detail'),
    path('dishes/create/', DishCreateView.as_view(), name='dish_create'),
    path('dishes/<int:pk>/update/', DishUpdateView.as_view(), name='dish_update'),
    path('dishes/<int:pk>/delete/', DishDeleteView.as_view(), name='dish_delete'),

    # Menu
    path('menus/', MenuListView.as_view(), name='menu_list'),
    path('menus/<int:pk>/', MenuDetailView.as_view(), name='menu_detail'),
    path('menus/create/', MenuCreateView.as_view(), name='menu_create'),
    path('menus/<int:pk>/update/', MenuUpdateView.as_view(), name='menu_update'),
    path('menus/<int:pk>/delete/', MenuDeleteView.as_view(), name='menu_delete'),

    # Category
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    # Ingredient
    path('ingredients/', IngredientListView.as_view(), name='ingredient_list'),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view(), name='ingredient_detail'),
    path('ingredients/create/', IngredientCreateView.as_view(), name='ingredient_create'),
    path('ingredients/<int:pk>/update/', IngredientUpdateView.as_view(), name='ingredient_update'),
    path('ingredients/<int:pk>/delete/', IngredientDeleteView.as_view(), name='ingredient_delete'),

    # Tag
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag_detail'),
    path('tags/create/', TagCreateView.as_view(), name='tag_create'),
    path('tags/<int:pk>/update/', TagUpdateView.as_view(), name='tag_update'),
    path('tags/<int:pk>/delete/', TagDeleteView.as_view(), name='tag_delete'),

    # Chef
    path('chefs/', ChefListView.as_view(), name='chef_list'),
    path('chefs/<int:pk>/', ChefDetailView.as_view(), name='chef_detail'),
    path('chefs/create/', ChefCreateView.as_view(), name='chef_create'),
    path('chefs/<int:pk>/update/', ChefUpdateView.as_view(), name='chef_update'),
    path('chefs/<int:pk>/delete/', ChefDeleteView.as_view(), name='chef_delete'),
]
