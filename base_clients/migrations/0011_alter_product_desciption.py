# Generated by Django 3.2.13 on 2022-06-14 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_clients', '0010_alter_product_desciption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desciption',
            field=models.TextField(max_length=50, null=True),
        ),
    ]