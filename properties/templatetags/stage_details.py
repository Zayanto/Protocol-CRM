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