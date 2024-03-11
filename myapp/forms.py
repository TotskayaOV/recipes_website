from django import forms
from .models import Chef, Post, Category, Product, ProductQuantity, CookingStep


class ChefRegistrationForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = ['username', 'nick_name', 'password', 'email', 'phone', 'about_me']
        labels = {'username': 'Логин',
                  'nick_name': 'Имя',
                  'password': 'пароль',
                  'email': 'электронная почта',
                  'phone': 'телефон',
                  'about_me': 'расскажите о себе'}
        exclude = ['last_login']

    username = forms.CharField(label='Логин для входа', max_length=10, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'укажите ваш логин'}))
    nick_name = forms.CharField(label='Подпись', max_length=20, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'укажите ваше имя'}))

    password = forms.CharField(widget=forms.PasswordInput())

    def save(self, commit=True):
        user = super(ChefRegistrationForm, self).save(commit=False)
        user.last_login = None
        if commit:
            user.save()
        return user


class PostForm(forms.ModelForm):
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), to_field_name='name')

    class Meta:
        model = Post
        fields = ['name', 'description', 'cooking_time', 'images', 'category_id']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['category_id'].label_from_instance = lambda obj: "%s" % obj.name


class CookingStepForm(forms.ModelForm):
    class Meta:
        model = CookingStep
        fields = ['description', 'images']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']


class ProductQuantityForm(forms.ModelForm):
    MEASUREMENT_CHOICES = [
        ('кг', 'килограмм'),
        ('литр', 'литр'),
        ('грамм', 'грамм'),
        ('столовая ложка', 'столовая ложка'),
        ('стакан', 'стакан'),
        ('чайная ложка', 'чайная ложка')
    ]

    measurement = forms.ChoiceField(choices=MEASUREMENT_CHOICES)
    product_id = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label=None, to_field_name='name', label='Продукт')

    class Meta:
        model = ProductQuantity
        fields = ['product_id', 'count', 'measurement']


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'description', 'cooking_time', 'images', 'category_id']
