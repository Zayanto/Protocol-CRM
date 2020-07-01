import arrow
import uuid
from django.db import models
from django_countries.fields import CountryField

from django.urls import reverse
from django.conf import settings
from properties.models import Property



class Tenant(models.Model):

    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    full_name = models.CharField("Full Name", max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=20, unique=True, null=True)
    description = models.TextField("Description", blank=True)
    country_of_origin = CountryField("Country of Origin", blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    created_on = models.DateTimeField(
        "Created on", auto_now_add=True, null=True)

    is_active = models.BooleanField(default=False)

    apartment = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    # contract = models.ForeignKey(
    #     Contract,
    #     on_delete=models.CASCADE,
    # )

    rent_tenant = models.CharField(
        "Rent he/she pays", max_length=10, blank=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        """"Return absolute URL to the Tenant Detail page."""
        return reverse('tenant_detail', kwargs={'pk': str(self.pk)})

    @property
    def created_on_arrow(self):
        return arrow.get(self.created_on).humanize()

    class Meta:
        ordering = ["-created_on"]
