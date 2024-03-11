from django.db import migrations, models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid


class Chef(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    nick_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    about_me = models.TextField()
    register_date = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'

@receiver(pre_save, sender=Chef)
def generate_unique_username(sender, instance, **kwargs):
    if not instance.username:
        current_time = timezone.now().strftime('%Y%m%d%H%M%S')
        random_uuid = str(uuid.uuid4().hex)[:5]
        instance.username = f'user_{current_time}_{random_uuid}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Post(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cooking_time = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='media/', null=True, blank=True)
    register_date = models.DateTimeField(auto_now=True)
    chef_id = models.ForeignKey(Chef, on_delete=models.SET('Анонимный шеф-повар'))
    category_id = models.ForeignKey(Category, on_delete=models.SET('Вне категорий'))
    product_id = models.ManyToManyField(Product)


class CookingStep(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    description = models.TextField()
    images = models.ImageField(upload_to='dish_images/', null=True, blank=True)


class ProductQuantity(models.Model):
    KG = 'кг'
    LITR = 'литр'
    GRAMM = 'грамм'
    TABLESPOON = 'столовая ложка'
    GLASS = 'стакан'
    TEASPOON = 'чайная ложка'

    MEASUREMENT_CHOICES = [
        (KG, 'килограмм'),
        (LITR, 'литр'),
        (GRAMM, 'грамм'),
        (TABLESPOON, 'столовая ложка'),
        (GLASS, 'стакан'),
        (TEASPOON, 'чайная ложка'),
    ]

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    count = models.DecimalField(max_digits=10, decimal_places=2)
    measurement = models.CharField(max_length=20, choices=MEASUREMENT_CHOICES)
