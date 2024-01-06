from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from core_apps.common.models import TimeStampedModel


User = get_user_model()


class Product(TimeStampedModel):
    # Define your Product model if not already defined
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Business(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="business")
    business_name = models.CharField(max_length=100, verbose_name=_("name"))
    projects = models.ManyToManyField(Product, related_name="businesses", blank=True)
    website = models.CharField(
        max_length=200, null=True, blank=True, verbose_name=_("website")
    )
    location = models.CharField(
        max_length=200, null=True, blank=True, verbose_name=_("location")
    )
    phone = models.CharField(max_length=20, verbose_name=_("phone"))
    # refers = models.ManyToManyField(Product, related_name='referred_by', blank=True)  # Allow an empty list

    def __str__(self):
        return self.business_name

    def add_product(self, product):
        self.projects.add(product)
