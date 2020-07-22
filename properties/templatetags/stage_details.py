from django import template

from properties.models import *

register = template.Library()

@register.simple_tag(takes_context=True)
def stage_opportunity(context):
    try:
        return StageOpportunity.objects.get(properties=context['property'])
    except:
        pass
    return None

@register.simple_tag(takes_context=True)
def stage_buying(context):
    try:
        return StageBuying.objects.get(properties=context['property'])
    except:
        pass
    return None

@register.simple_tag(takes_context=True)
def stage_renovation(context):
    try:
        return StageRenovation.objects.get(properties=context['property'])
    except:
        pass
    return None

@register.simple_tag(takes_context=True)
def stage_rent(context):
    try:
        return StageForRent.objects.get(properties=context['property'])
    except:
        pass
    return None

@register.simple_tag(takes_context=True)
def stage_tenant(context):
    try:
        return StageWithTenant.objects.get(properties=context['property'])
    except:
        pass
    return None

@register.simple_tag()
def stage_opportunity_list(property_):
    try:
        return StageOpportunity.objects.get(properties=property_)
    except:
        pass
    return None

@register.simple_tag(takes_context=True)
def renovation_teams(context):
    try:
        propert = context['property']
        return propert.stagerenovation.renovationteam_set.all()
    except:
        pass
    return None

@register.simple_tag(takes_context=True)
def all_contracts_modal(context):
    try:
        propert = context['property']
        return propert.contract_set.filter(monthly_property_expense_track=False)
    except:
        pass
    return None

@register.simple_tag(takes_context=True)
def all_contracts_tab(context):
    try:
        propert = context['property']
        return propert.contract_set.filter(monthly_property_expense_track=True)
    except:
        pass
    return None

@register.simple_tag(takes_context=True)
def monthly_maintenance_model_list(context):
    try:
        propert = context['property']
        return propert.monthly_maintenance_model.all()
    except:
        pass
    return None

@register.simple_tag(takes_context=True)
def monthly_maintenance_model_count(context):
    try:
        propert = context['property']
        return propert.monthly_maintenance_model.count()
    except:
        pass
    return None

@register.simple_tag(takes_context=True)
def tenant_monthly_maintenance_model_count(context):
    try:
        propert = context['property']
        return list(TenantMonthlyMaintenanceModel.objects.filter(contract__apartment=propert).values_list('id', flat=True))
    except:
        pass
    return None

@register.simple_tag
def tenant_monthly_maintenance_model_list(contract):
    try:
        return contract.tenant_monthly_maintenance_model.all()
    except:
        pass
    return None

@register.simple_tag(takes_context=True)
def expense_tables(context):
    try:
        propert = context['property']
        renovation_teams = propert.stagerenovation.renovationteam_set.all()
        return ExpenseTable.objects.filter(renovation_team__in=renovation_teams)
    except:
        pass
    return None

@register.simple_tag(takes_context=True)
def expense_tables_count(context):
    try:
        propert = context['property']
        renovation_teams = propert.stagerenovation.renovationteam_set.all()
        return ExpenseTable.objects.filter(renovation_team__in=renovation_teams).count()
    except:
        pass
    return None

@register.simple_tag()
def stage_buying_list(property_):
    try:
        return StageBuying.objects.get(properties=property_)
    except:
        pass
    return None


@register.simple_tag()
def stage_rent_list(property_):
    try:
        return StageForRent.objects.get(properties=property_)
    except:
        pass
    return None

@register.simple_tag()
def stage_tenant_list(property_):
    try:
        return StageWithTenant.objects.get(properties=property_)
    except:
        pass
    return None

@register.simple_tag()
def property_tenant(property_):
    try:
        return property_.reviews.all()[0]
    except:
        pass
    return None

@register.simple_tag()
def property_tenant_contract(property_):
    try:
        return property_.reviews.all()[0].contract_set.all()[0]
    except:
        pass
    return None
