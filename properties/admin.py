from django.contrib import admin
from properties.models import *

admin.site.register(Property)
admin.site.register(PropertyImage)
admin.site.register(StageOpportunity)
admin.site.register(StageBuying)
admin.site.register(StageForRent)
admin.site.register(StageWithTenant)
admin.site.register(StageRenovation)
admin.site.register(RenovationTeam)
admin.site.register(RenovationTeamExpenses)
admin.site.register(ExpenseTable)

