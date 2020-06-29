import arrow
import uuid
from django.db import models

from datetime import datetime
from django.urls import reverse
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model  # new
from tenants.models import Tenant
from properties.models import Property


class Contract(models.Model):

    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    title = models.CharField(max_length=2000, null=True)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    end_date = models.DateTimeField(blank=True)
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
    )
    apartment = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        null=True
    )

    rent_tenant = models.CharField(
        "Rent he/she pays", max_length=10, blank=True)

    class ContractStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        PENDING = "pending", "Pending"
        INACTIVE = "inactive", "Inactive"

    contract_status = models.CharField("Status", max_length=20,
                                       choices=ContractStatus.choices, default=ContractStatus.ACTIVE)

    class ContractPaymentStatus(models.TextChoices):
        PAID = "paid", "Paid"
        UNPAID = "unpaid", "Unpaid"

    contract_payment_status = models.CharField("Payment Status", max_length=20,
                                               choices=ContractPaymentStatus.choices, default=ContractPaymentStatus.UNPAID)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """"Return absolute URL to the Contact Detail page."""
        return reverse('contract:contract_detail', kwargs={'pk': str(self.pk)})

    @property
    def created_on_arrow(self):
        return arrow.get(self.created_on).humanize()
