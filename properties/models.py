import arrow
import uuid
from django.db import models

from datetime import datetime
from django.urls import reverse
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model  
from django.utils import timezone

def monthly_maintenance_document_file_path(instance, filename):
    model_name = instance.__class__.__name__
    today = datetime.now()
    name = f'{model_name}/{instance.id}/{today.year}/{filename}'
    return name

class Property(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """"Return absolute URL to the Property Detail page."""
        return reverse('property:property_detail', kwargs={"pk": str(self.pk)})

    @property
    def created_on_arrow(self):
        return arrow.get(self.created_on).humanize()

    def first_photo(self):
        return self.images.first()

    class Meta:  # new
        permissions = [
            ('special_status', 'Can read all books'),
        ]

class StageOpportunity(models.Model):
    
    class Destination(models.TextChoices):
        BIROURI = "birouri", "Birouri"
        REZIDENTIAL = "rezidentaial", "Rezidential"
        COMERCIAL = "comercial", "Comercial"
    
    class Layout(models.TextChoices):
        DECOMANDAT = "decomandat", "Decomandat"
        SEMIDECOMANDAT = "semidecomandat", "Semidecomandat"
        NEDECOMANDAT = "nedecomandat", "Nedecomandat"
        CIRCULAR = "circular", "Circular"
        VAGON = "vagon", "Vagon"
    class ComfortType(models.TextChoices):
        UNU = "1", "1"
        DOI = "2", "2"
        TREI = "3", "3"
        LUX = "lux", "Lux"
    class InteriorState(models.TextChoices):
        OTHER = "other", "Other"
        NECESITA_RENOVARE = "necesita-renovare", "Necesita-Renovare"
        RENOVAT = "renovat", "Renovat"
        NOU = "nou", "Nou"
        CARAMIDA = "caramida", "Caramida"
    class BuildingType(models.TextChoices):
        BETON = "beton", "Beton"
        CARAMIDA = "caramida", "Caramida"
        LEMN = "lemn", "Lemn"
        BCA = "bca", "Bca"
        METAL = "metal", "Metal"
        OTHER = "other", "Other"

    properties = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='stage_opportunity', null=True, blank=True)
    owner = models.CharField(max_length=200, null=True, blank=True)
    asking_price = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    residence_complex = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    zipcode = models.CharField(max_length=200, null=True, blank=True)
    building = models.CharField(max_length=200, null=True, blank=True)
    entrance = models.CharField(max_length=200, null=True, blank=True)
    floor = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    apartament_number = models.CharField(max_length=200, null=True, blank=True)
    reper = models.CharField(max_length=200, null=True, blank=True)
    vecinatati = models.CharField(max_length=200, null=True, blank=True)
    usable_sqm = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    build_sqm = models.DecimalField(max_digits=10, decimal_places=1,  null=True, blank=True)
    destination = models.CharField("Destination", max_length=20, choices=Destination.choices, default=Destination.REZIDENTIAL)
    layout = models.CharField("Layout", max_length=20, choices=Layout.choices, default=Layout.DECOMANDAT)
    comfort_type = models.CharField("Comfort Type", max_length=20, choices=ComfortType.choices, default=ComfortType.UNU)
    interior_state = models.CharField("Interior State", max_length=20, choices=InteriorState.choices, default=InteriorState.OTHER)
    number_of_rooms = models.IntegerField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    kitchen = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    balcony = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)
    building_type = models.CharField("Building Type", max_length=20,choices=BuildingType.choices, default=BuildingType.BETON)
    building_construction_date = models.DateTimeField(null=True, blank=True)
    basement = models.BooleanField(default=True)
    potential_rent = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    description = models.TextField(blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_building_construction_date(self):
        if self.building_construction_date:
            return datetime.strftime(self.building_construction_date, '%Y-%m-%d')

class StageBuying(models.Model):
    properties = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='stage_buying', null=True, blank=True)
    # Expenses
    agent_costs = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    notary_costs = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    legal_costs = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    accountant_costs = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    other_costs = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    buy_price = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    description = models.TextField(blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class StageRenovation(models.Model):
    properties = models.OneToOneField(Property, on_delete=models.CASCADE, null=True)
    investor = models.CharField(max_length=200, null=True)
    renovation_budget = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    date_receiving_money = models.DateTimeField(null=True)
    date_receiving_key = models.DateTimeField(null=True)
    description = models.TextField(null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_date_receiving_money(self):
        if self.date_receiving_money:
            return datetime.strftime(self.date_receiving_money, '%Y-%m-%d')
    
    def get_date_receiving_key(self):
        if self.date_receiving_key:
            return datetime.strftime(self.date_receiving_key, '%Y-%m-%d')

class RenovationTeam(models.Model):
    renovation_stage = models.ForeignKey(StageRenovation, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=200, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class ExpenseTable(models.Model):
    renovation_team = models.ForeignKey(RenovationTeam, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
class RenovationTeamExpenses(models.Model):
    #Expense Table Content
    expense_table = models.ForeignKey(ExpenseTable, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    currency = models.CharField(max_length=200, null=True)
    account = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(blank=True)
    store = models.CharField(max_length=200, null=True, blank=True)
    order_date = models.DateTimeField(blank=True)
    delivery_date = models.DateTimeField(blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class StageForRent(models.Model):
    properties = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='stage_rent', null=True, blank=True)
    expected_rent = models.IntegerField(null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class StageWithTenant(models.Model):
    properties = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='stage_tenant', null=True, blank=True)
    actual_rent = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    description = models.TextField(blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class PropertyImage(models.Model):
    properties = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='properties/', blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class MonthlyMaintenanceModel(models.Model):
    properties = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, related_name='monthly_maintenance_model')
    name = models.CharField(max_length=200, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class MonthlyMaintenance(models.Model):
    monthly_maintenance_model = models.ForeignKey(MonthlyMaintenanceModel, on_delete=models.CASCADE, null=True, related_name='monthly_maintenance')

    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True, default=0)
    currency = models.CharField(max_length=200, null=True, blank=True)
    account = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(null=True, default=timezone.now)
    document = models.FileField(null=True, blank=True, upload_to=monthly_maintenance_document_file_path)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
 

class TenantMonthlyMaintenanceModel(models.Model):
    from contracts.models import Contract
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, related_name='tenant_monthly_maintenance_model')
    name = models.CharField(max_length=200, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class TenantMonthlyMaintenance(models.Model):
    tenant_monthly_maintenance_model = models.ForeignKey(TenantMonthlyMaintenanceModel, on_delete=models.CASCADE, null=True, related_name='tenant_monthly_maintenance')
    
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True, default=0)
    currency = models.CharField(max_length=200, null=True, blank=True)
    account = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(null=True, default=timezone.now)
    document = models.FileField(null=True, blank=True, upload_to=monthly_maintenance_document_file_path)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)