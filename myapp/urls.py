from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns =[
    path('', views.home, name='home'),
    path('home', views.home, name='about'),
    path('categories/', views.category_list, name='category_list'),
    path('category_recipes/<int:category_id>/', views.category_recipes, name='category_recipes'),
    path('recipe_details/<int:recipe_id>/', views.recipe_details, name='recipe_details'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', views.register_chef, name='register_chef'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('add_product_to_recipe/<int:post_id>/', views.add_product_to_recipe, name='add_product_to_recipe'),
    path('add_steps_to_recipe/<int:post_id>/', views.add_steps_to_recipe, name='add_steps_to_recipe'),
    path('chef_recipes/<int:chef_id>/', views.chef_recipes, name='chef_recipes'),
    path('my_recipes/', views.my_recipes, name='my_recipes'),
    path('all_recipes/', views.all_recipes, name='all_recipes'),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('recipe_detail/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]

