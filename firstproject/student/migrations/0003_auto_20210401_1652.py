# Generated by Django 3.1.7 on 2021-04-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210401_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlog',
            name='password',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='studentlog',
            name='username',
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='course',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='password',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='username',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
