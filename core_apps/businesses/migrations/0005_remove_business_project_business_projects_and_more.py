# Generated by Django 4.1.7 on 2023-12-27 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("businesses", "0004_alter_business_project"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="business",
            name="project",
        ),
        migrations.AddField(
            model_name="business",
            name="projects",
            field=models.ManyToManyField(
                related_name="businesses", to="businesses.product"
            ),
        ),
        migrations.RemoveField(
            model_name="business",
            name="refers",
        ),
        migrations.AlterField(
            model_name="business",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="business",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="business",
            name="refers",
            field=models.ManyToManyField(
                related_name="referred_by", to="businesses.product"
            ),
        ),
    ]