from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Chef, Product, Category, Post, ProductQuantity, CookingStep
from .forms import ChefRegistrationForm, PostForm, ProductForm, ProductQuantityForm, CookingStepForm, EditPostForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist

from django.utils import timezone

default_value = timezone.now


def home(request):
    text_html = """
    <h1>Добро пожаловать на сайт!</h1>
    <p>Здесь собраны рецепты из простых продуктов, которые обычно входят в диетическое питание.</p>
    """
    return render(request, 'index.html', {'content': text_html})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def category_recipes(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = Post.objects.filter(category_id=category)
    return render(request, 'category_recipes.html', {'category': category, 'recipes': recipes})


def recipe_details(request, recipe_id):
    recipe = get_object_or_404(Post, id=recipe_id)
    cooking_steps = CookingStep.objects.filter(post_id=recipe)
    product_quantities = ProductQuantity.objects.filter(post_id=recipe)
    return render(request, 'recipe_details.html',
                  {'recipe': recipe, 'cooking_steps': cooking_steps, 'product_quantities': product_quantities})


def register_chef(request):
    if request.method == 'POST':
        form = ChefRegistrationForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            new_user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=make_password(user_data['password'])
            )
            new_user.save()
            login(request, new_user)
            return redirect('/')
    else:
        form = ChefRegistrationForm()
    return render(request, 'registration.html', {'form': form})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            current_user = request.user
            post.chef_id = current_user
            post.save()
            return redirect('add_product_to_recipe', post_id=post.id)
    else:
        post_form = PostForm()
    return render(request, 'add_recipe.html', {'post_form': post_form})


@login_required
def add_product_to_recipe(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        product_quantity_form = ProductQuantityForm(request.POST)
        if product_quantity_form.is_valid():
            product_quantity = product_quantity_form.save(commit=False)
            product_name = request.POST.get('product_id')
            try:
                product = Product.objects.get(name=product_name)
            except Product.DoesNotExist:
                product_quantity_form.add_error('product_id', 'Выберите существующий продукт из списка.')
                return render(request, 'add_product_to_recipe.html', {'product_quantity_form': product_quantity_form})
            product_quantity.product_id = product
            product_quantity.post_id = post
            product_quantity.save()
            if "add_product" in request.POST:
                return redirect('add_product_to_recipe', post_id=post_id)
            elif "add_steps" in request.POST:
                return redirect('add_steps_to_recipe', post_id=post_id)
    else:
        product_quantity_form = ProductQuantityForm()
    return render(request, 'add_product_to_recipe.html', {'product_quantity_form': product_quantity_form})


@login_required
def add_steps_to_recipe(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        cooking_step_form = CookingStepForm(request.POST, request.FILES)
        if cooking_step_form.is_valid():
            cooking_step = cooking_step_form.save(commit=False)
            cooking_step.post_id = post
            cooking_step.save()
            if "add_product" in request.POST:
                return redirect('add_steps_to_recipe',
                            post_id=post_id)  # Перенаправление на ту же форму для добавления следующего шага
            elif "add_steps" in request.POST:
                return redirect('/')
    else:
        cooking_step_form = CookingStepForm()
    return render(request, 'add_steps_to_recipe.html', {'cooking_step_form': cooking_step_form})


@login_required
def edit_recipe(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('recipe_details', recipe_id=post_id)
    else:
        form = EditPostForm(instance=post)
    return render(request, 'edit_recipe.html', {'form': form, 'post': post})


def chef_recipes(request, chef_id):
    chef_posts = Post.objects.filter(chef_id=chef_id)
    return render(request, 'chef_recipes.html', {'chef_posts': chef_posts})


def my_recipes(request):
    current_user = request.user
    chef_posts = Post.objects.filter(chef_id=current_user.id)
    return render(request, 'my_recipes.html', {'chef_posts': chef_posts})


def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Post, id=recipe_id)
    if request.user == recipe.chef_id:
        if request.method == 'POST':
            pass
        else:
            form = EditPostForm(instance=recipe)
        return render(request, 'edit_recipe.html', {'form': form, 'recipe': recipe})
    else:
        return HttpResponse('У вас нет прав для редактирования этого рецепта.')

