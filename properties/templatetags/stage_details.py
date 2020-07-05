from django import template

from properties.models import *

register = template.Library()

@register.simple_tag(takes_context=True)
def stage_opportunity(context):
    stage_opportunity, _ = StageOpportunity.objects.get_or_create(properties=context['property'])
    print(stage_opportunity)
    return stage_opportunity

@register.simple_tag(takes_context=True)
def stage_buying(context):
    stage_buying, _ = StageOpportunity.objects.get_or_create(properties=context['property'])
    return stage_buying

@register.simple_tag(takes_context=True)
def stage_rent(context):
    stage_rent, _ = StageOpportunity.objects.get_or_create(properties=context['property'])
    return stage_rent

@register.simple_tag(takes_context=True)
def stage_tenant(context):
    stage_tenant, _ = StageOpportunity.objects.get_or_create(properties=context['property'])
    return stage_tenant