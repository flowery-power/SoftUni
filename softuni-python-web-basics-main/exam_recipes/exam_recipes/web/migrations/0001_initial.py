# Generated by Django 4.0.2 on 2022-02-09 21:15

from django.db import migrations, models
import exam_recipes.web.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('ingredients', models.CharField(max_length=250)),
                ('cooking_time', models.IntegerField(validators=[exam_recipes.web.validators.validate_time_value])),
            ],
        ),
    ]