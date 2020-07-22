from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from properties.api.views import *

app_name='property-api'

urlpatterns = [
    path('properties/create-property-stage-opportunity/', CreatePropertyStageOpportunityAPIView.as_view(), name='create-property-stage-opportunity'),
    path('properties/stage-renovation/', StageRenovationAPIView.as_view(), name='stage-renovation'),
    path('properties/stage-opportunity/', StageOpportunityAPIView.as_view(), name='stage-opportunity'),
    path('properties/stage-buying/', StageBuyingAPIView.as_view(), name='stage-buying'),
    path('properties/stage-rent/', StageRentAPIView.as_view(), name='stage-rent'),
    path('properties/stage-tenant/', StageTenantAPIView.as_view(), name='stage-tenant'),
    path('properties/renovation-team-create/', RenovationTeamCreateView.as_view(), name='renovation-team-create'),
    path('properties/renovation-team-update/', RenovationTeamUpdateView.as_view(), name='renovation-team-update'),
    path('properties/expense-table-create/', ExpenseTableCreateView.as_view(), name='expense-table-create'),
    path('properties/renovation-team-list/', RenovationTeamListDatatableAPIView.as_view(), name='renovation-team-list'),
    path('properties/renovation-team-expenses-create/', RenovationTeamExpenseCreateView.as_view(), name='renovation-team-expenses-create'),
    path('properties/renovation-team-expenses-list/', RenovationTeamExpensesDatatableAPIView.as_view(), name='renovation-team-expenses-list'),
    path('properties/add-contract-in-monthly-expense/', AddContractInMonthlyExpense.as_view(), name='add-contract-in-monthly-expense'),
    path('properties/create-tenant-monthly-maintenance-model/', CreateTenantMonthlyMaintenanceModel.as_view(), name='create-tenant-monthly-maintenance-model'),
    path('properties/create-monthly-maintenance-model/', CreateMonthlyMaintenanceModel.as_view(), name='create-monthly-maintenance-model'),
    path('properties/monthly-maintenance-list/', MonthlyMaintenanceDatatableAPIView.as_view(), name='monthly-maintenance-list'),
    path('properties/tenant-monthly-maintenance-list/', TenantMonthlyMaintenanceDatatableAPIView.as_view(), name='tenant-monthly-maintenance-list'),
    path('properties/monthly-maintenance-create/', MonthlyMaintenanceCreateView.as_view(), name='monthly-maintenance-create'),
    path('properties/tenant-monthly-maintenance-create/', TenantMonthlyMaintenanceCreateView.as_view(), name='tenant-monthly-maintenance-create'),
]
