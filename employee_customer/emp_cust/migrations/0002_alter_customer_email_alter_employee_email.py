# Generated by Django 5.0.1 on 2024-02-29 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_cust', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
