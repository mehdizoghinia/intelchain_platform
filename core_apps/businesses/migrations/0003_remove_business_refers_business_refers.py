# Generated by Django 4.1.7 on 2023-12-27 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("businesses", "0002_rename_name_business_business_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="business",
            name="refers",
        ),
        migrations.AddField(
            model_name="business",
            name="refers",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="referred_by",
                to="businesses.product",
            ),
        ),
    ]