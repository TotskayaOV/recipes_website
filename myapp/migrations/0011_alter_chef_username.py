# Generated by Django 5.0.2 on 2024-03-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_chef_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='username',
            field=models.CharField(default='default_username', max_length=10, unique=True),
        ),
    ]
