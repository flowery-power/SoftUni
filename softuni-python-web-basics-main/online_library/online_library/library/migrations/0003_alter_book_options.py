# Generated by Django 4.0.2 on 2022-02-25 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['type', 'title']},
        ),
    ]