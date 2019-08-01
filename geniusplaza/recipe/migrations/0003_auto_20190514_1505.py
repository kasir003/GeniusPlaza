# Generated by Django 2.2.1 on 2019-05-14 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20190514_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_recipe', to=settings.AUTH_USER_MODEL),
        ),
    ]