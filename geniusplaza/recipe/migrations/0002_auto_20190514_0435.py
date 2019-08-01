# Generated by Django 2.2.1 on 2019-05-14 04:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(help_text='Receipe ID', on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_recipe', to='recipe.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='step',
            name='recipe',
            field=models.ForeignKey(help_text='Receipe ID', on_delete=django.db.models.deletion.CASCADE, related_name='step_recipe', to='recipe.Recipe'),
        ),
    ]
