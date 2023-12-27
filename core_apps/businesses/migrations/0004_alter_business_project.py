# Generated by Django 4.1.7 on 2023-12-27 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("businesses", "0003_remove_business_refers_business_refers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="business",
            name="project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="businesses",
                to="businesses.product",
            ),
        ),
    ]
