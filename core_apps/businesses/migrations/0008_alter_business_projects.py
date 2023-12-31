# Generated by Django 4.1.7 on 2023-12-27 14:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("businesses", "0007_remove_business_refers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="business",
            name="projects",
            field=models.ManyToManyField(
                blank=True, related_name="businesses", to="businesses.product"
            ),
        ),
    ]
