import arrow
import uuid
from django.db import models

from datetime import datetime
from django.urls import reverse
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model  #


class StageOpportunity(models.Model):

    owner = models.CharField(max_length=200, null=True)
    asking_price = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    residence_complex = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    building = models.CharField(max_length=200, null=True)
    entrance = models.CharField(max_length=200, null=True)
    floor = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    apartament_number = models.CharField(max_length=200, null=True)
    reper = models.CharField(max_length=200, null=True)
    vecinatati = models.CharField(max_length=200, null=True)

    usable_sqm = models.DecimalField(
        max_digits=10, decimal_places=1, null=True)

    build_sqm = models.DecimalField(
        max_digits=10, decimal_places=1,  null=True)

    class Destination(models.TextChoices):
        BIROURI = "birouri", "Birouri"
        REZIDENTIAL = "rezidentaial", "Rezidential"
        COMERCIAL = "comercial", "Comercial"

    destination = models.CharField("Destination", max_length=20,
                                   choices=Destination.choices, default=Destination.REZIDENTIAL)

    class Layout(models.TextChoices):
        DECOMANDAT = "decomandat", "Decomandat"
        SEMIDECOMANDAT = "semidecomandat", "Semidecomandat"
        NEDECOMANDAT = "nedecomandat", "Nedecomandat"
        CIRCULAR = "circular", "Circular"
        VAGON = "vagon", "Vagon"

    layout = models.CharField("Layout", max_length=20,
                              choices=Layout.choices, default=Layout.DECOMANDAT)

    class ComfortType(models.TextChoices):
        UNU = "1", "1"
        DOI = "2", "2"
        TREI = "3", "3"
        LUX = "lux", "Lux"

    comfort_type = models.CharField("Comfort Type", max_length=20,
                                    choices=ComfortType.choices, default=ComfortType.UNU)

    class InteriorState(models.TextChoices):
        OTHER = "other", "Other"
        NECESITA_RENOVARE = "necesita-renovare", "Necesita-Renovare"
        RENOVAT = "renovat", "Renovat"
        NOU = "nou", "Nou"
        CARAMIDA = "caramida", "Caramida"

    interior_state = models.CharField("Interior State", max_length=20,
                                      choices=InteriorState.choices, default=InteriorState.OTHER)

    number_of_rooms = models.IntegerField(null=True)
    bedrooms = models.IntegerField(null=True)
    kitchen = models.IntegerField(null=True)
    bathrooms = models.IntegerField(null=True)
    balcony = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)

    class BuildingType(models.TextChoices):
        BETON = "beton", "Beton"
        CARAMIDA = "caramida", "Caramida"
        LEMN = "lemn", "Lemn"
        BCA = "bca", "Bca"
        METAL = "metal", "Metal"
        OTHER = "other", "Other"

    building_type = models.CharField("Building Type", max_length=20,
                                     choices=BuildingType.choices, default=BuildingType.BETON)
    building_construction_date = models.DateTimeField(null=True, blank=True)
    basement = models.BooleanField(default=True)
    potential_rent = models.DecimalField(
        max_digits=10, decimal_places=1, null=True)
    description = models.TextField(blank=True)


class StageBuying(models.Model):

    # Expenses
    agent_costs = models.DecimalField(
        max_digits=10, decimal_places=1, null=True)
    notary_costs = models.DecimalField(
        max_digits=10, decimal_places=1, null=True)
    legal_costs = models.DecimalField(
        max_digits=10, decimal_places=1, null=True)
    accountant_costs = models.DecimalField(
        max_digits=10, decimal_places=1, null=True)
    other_costs = models.DecimalField(
        max_digits=10, decimal_places=1, null=True)
    buy_price = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    description = models.TextField(blank=True)

    # User needs to add other costs in the future. So this needs to be dynamic I think.


class StageRenovation(models.Model):

    investor = models.CharField(max_length=200, null=True)
    renovation_budget = models.DecimalField(
        max_digits=10, decimal_places=1, null=True)
    date_receiving_money = models.DateTimeField(blank=True)
    date_receiving_key = models.DateTimeField(blank=True)
    description = models.TextField(blank=True)


class StageForRent(models.Model):
    expected_rent = models.IntegerField(null=True)


class StageWithTenant(models.Model):
    actual_rent = models.DecimalField(
        max_digits=10, decimal_places=1, null=True)
    description = models.TextField(blank=True)


class Property(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    title = models.CharField(max_length=200, null=True)

    # photo_main = models.ImageField(upload_to='properties/', blank=True)
    # photo_1 = models.ImageField(upload_to='properties/', blank=True)
    # photo_2 = models.ImageField(upload_to='properties/', blank=True)
    # photo_3 = models.ImageField(upload_to='properties/', blank=True)
    # photo_4 = models.ImageField(upload_to='properties/', blank=True)
    # photo_5 = models.ImageField(upload_to='properties/', blank=True)
    # photo_6 = models.ImageField(upload_to='properties/', blank=True)
    # photo_7 = models.ImageField(upload_to='properties/', blank=True)
    # photo_8 = models.ImageField(upload_to='properties/', blank=True)
    # photo_9 = models.ImageField(upload_to='properties/', blank=True)
    # photo_10 = models.ImageField(upload_to='properties/', blank=True)
    # photo_11 = models.ImageField(upload_to='properties/', blank=True)
    # photo_12 = models.ImageField(upload_to='properties/', blank=True)

    description = models.TextField(blank=True)

    list_date = models.DateTimeField(default=datetime.now, blank=True)



    def get_absolute_url(self):
        """"Return absolute URL to the Property Detail page."""
        return reverse('property:property_detail', kwargs={"pk": str(self.pk)})

    @ property
    def created_on_arrow(self):
        return arrow.get(self.created_on).humanize()

    def first_photo(self):
        return self.images.first()

    class Meta:  # new
        permissions = [
            ('special_status', 'Can read all books'),
        ]

class PropertyImage(models.Model):
    image = models.ImageField(upload_to='properties/', blank=True)
    _property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
