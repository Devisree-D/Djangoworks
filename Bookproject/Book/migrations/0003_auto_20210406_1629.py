# Generated by Django 3.1.7 on 2021-04-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_auto_20210401_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]