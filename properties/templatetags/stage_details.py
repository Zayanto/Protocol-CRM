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
