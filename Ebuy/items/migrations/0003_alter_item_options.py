# Generated by Django 5.0.7 on 2024-08-08 11:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0002_alter_categories_options_item"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="item",
            options={"ordering": ("Name",), "verbose_name_plural": "items"},
        ),
    ]
