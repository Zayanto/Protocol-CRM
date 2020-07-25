import arrow
import uuid
from django.db import models

from datetime import datetime
from django.urls import reverse
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model


class Payment(models.Model):

    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    title = models.CharField(max_length=2000, null=True)

    class Status(models.TextChoices):
        UPCOMING = "upcoming", "Upcoming"
        UNPAID = "unpaid", "Unpaid"
        SENT = "sent", "Sent"
        PAID = "paid", "Paid"

    status = models.CharField("Status", max_length=20,
                                   choices=Status.choices, default=Status.UNPAID)
    
    invoice_start_date = models.DateTimeField(null=True, blank=True)
    invoice_end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """"Return absolute URL to the Property Detail page."""
        return reverse('payment_detail', kwargs={"pk": str(self.pk)})

    @ property
    def created_on_arrow(self):
        return arrow.get(self.created_on).humanize()

   
