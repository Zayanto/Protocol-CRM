import arrow
import uuid
from django.db import models

from datetime import datetime
from django.urls import reverse
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model


class Owner(models.Model):

    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    title = models.CharField(max_length=2000, null=True)

    class Type(models.TextChoices):
        INVESTOR = "investor", "Investor"
        NORMAL = "normal", "Normal"

    owner_type = models.CharField("Type", max_length=20,
                               choices=Type.choices, default=Type.NORMAL)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """"Return absolute URL to the Contact Detail page."""
        return reverse('owner_detail', kwargs={'pk': str(self.pk)})

    @property
    def created_on_arrow(self):
        return arrow.get(self.created_on).humanize()
