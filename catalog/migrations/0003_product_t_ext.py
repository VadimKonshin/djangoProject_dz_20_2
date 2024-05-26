# Generated by Django 5.0.6 on 2024-05-26 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_product_manufactured_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="t_ext",
            field=models.TextField(
                blank=True,
                help_text="Введите описание категории",
                null=True,
                verbose_name="Описание категории",
            ),
        ),
    ]