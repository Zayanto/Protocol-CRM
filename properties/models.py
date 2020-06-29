import arrow
import uuid
from django.db import models

from datetime import datetime
from django.urls import reverse
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model  # new


class Property(models.Model):

    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    title = models.CharField(max_length=2000, null=True)

    # Localizare
    residence_complex = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    street_number = models.IntegerField()
    zipcode = models.CharField(max_length=200, null=True)
    building = models.CharField(max_length=200, null=True)
    entrance = models.CharField(max_length=200, null=True)
    apartament = models.CharField(max_length=200, null=True)
    reper = models.CharField(max_length=200, null=True)
    vecinatati = models.CharField(max_length=200, null=True)

    # Caracteristici

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

    floor = models.DecimalField(max_digits=10, decimal_places=1, null=True)

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
    building_age = models.IntegerField()
    usable_sqm = models.DecimalField(
        max_digits=10, decimal_places=1, null=True)
    build_sqm = models.DecimalField(
        max_digits=10, decimal_places=1,  null=True)

    # Incaperi si Anexe

    rooms = models.IntegerField(null=True)
    bedrooms = models.IntegerField(null=True)
    kitchen = models.IntegerField(null=True)
    bathrooms = models.IntegerField(null=True)
    balcony = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)

  

    # Caracteristici Imobil

    class BuildingType(models.TextChoices):
        BETON = "beton", "Beton"
        CARAMIDA = "caramida", "Caramida"
        LEMN = "lemn", "Lemn"
        BCA = "bca", "Bca"
        METAL = "metal", "Metal"
        OTHER = "other", "Other"

    building_type = models.CharField("Building Type", max_length=20,
                                     choices=BuildingType.choices, default=BuildingType.BETON)
    construction_date = models.DateTimeField(null=True, blank=True)

    class ConstructionType(models.TextChoices):
        HOUSE = "house", "House"
        MIXT_BUILDING = "mix-building", "Mix-Building"
        STUDIO_BUILDING = "studio-building", "Studio-Building"

    construction_type = models.CharField("Construction Type", max_length=20,
                                         choices=ConstructionType.choices, default=ConstructionType.MIXT_BUILDING)

    basement = models.BooleanField(default=True)
    notes = models.TextField(blank=True)
    lot_size = models.DecimalField(max_digits=10, decimal_places=1)

    # Dotari si Utilitati

    # Pret

    buy_price = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    sell_price = models.DecimalField(
        max_digits=10, decimal_places=1, null=True)
    rent = models.DecimalField(max_digits=10, decimal_places=1, null=True)

    # Poze

    photo_main = models.ImageField(upload_to='properties/', blank=True)
    photo_1 = models.ImageField(upload_to='properties/', blank=True)
    photo_2 = models.ImageField(upload_to='properties/', blank=True)
    photo_3 = models.ImageField(upload_to='properties/', blank=True)
    photo_4 = models.ImageField(upload_to='properties/', blank=True)
    photo_5 = models.ImageField(upload_to='properties/', blank=True)
    photo_6 = models.ImageField(upload_to='properties/', blank=True)
    photo_7 = models.ImageField(upload_to='properties/', blank=True)
    photo_8 = models.ImageField(upload_to='properties/', blank=True)
    photo_9 = models.ImageField(upload_to='properties/', blank=True)
    photo_10 = models.ImageField(upload_to='properties/', blank=True)
    photo_11 = models.ImageField(upload_to='properties/', blank=True)
    photo_12 = models.ImageField(upload_to='properties/', blank=True)

    description = models.TextField(blank=True)

    # Listing Details

    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """"Return absolute URL to the Property Detail page."""
        return reverse('property:property_detail', kwargs={"pk": str(self.pk)})

    @ property
    def created_on_arrow(self):
        return arrow.get(self.created_on).humanize()

    class Meta:  # new
        permissions = [
            ('special_status', 'Can read all books'),
        ]


class Comment(models.Model):  # new

    property_comment = models.ManyToManyField(
        Property, related_name='comments')
    comment = models.CharField(max_length=500)

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

# class UnderRenovation(models.Model):

    # renovation_budget =
    # date_receiving_money =
    # date_receiving_key =
    # renovation_start_date =
