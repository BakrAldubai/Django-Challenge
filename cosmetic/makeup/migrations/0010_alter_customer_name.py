# Generated by Django 4.0.1 on 2022-02-08 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0009_alter_brand_name_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]