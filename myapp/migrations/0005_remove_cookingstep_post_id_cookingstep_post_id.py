# Generated by Django 5.0.2 on 2024-02-25 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_cookingstep_image_remove_post_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cookingstep',
            name='post_id',
        ),
        migrations.AddField(
            model_name='cookingstep',
            name='post_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.post'),
        ),
    ]
