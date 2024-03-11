from django.contrib import admin
from .models import Chef, Product, Category, CookingStep, Post
from django.utils.html import format_html


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ['username', 'nick_name', 'email', 'phone', 'about_me', 'register_date']
    fieldsets = (('основные данные', {'fields': ['username', 'nick_name']}),
                 ('контактные данные', {'fields': ['email', 'phone']}),
                 ('дополнительная информация', {'fields': ['about_me', 'register_date'], 'classes': ['collapse']}),)
    exclude = ['register_date']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('register_date',)
        return self.readonly_fields


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['name', 'description']
    fieldsets = (
        ('основные данные продукта', {'fields': ['name']}),
        ('С1', {'fields': ['description']}),
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        else:
            return format_html('<img src="/media/product_images/no_to_foto.png" width="50" height="50" />')

    display_image.short_description = 'Фото продукта'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'cooking_time', 'images']
    fieldsets = (
        ('основные данные заказа', {'fields': ['name', 'description', 'cooking_time']}),
        ('список продуктов', {'fields': ['images']}),
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        else:
            return format_html('<img src="/media/product_images/no_to_foto.png" width="50" height="50" />')

    display_image.short_description = 'Фото продукта'

