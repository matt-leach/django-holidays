from django import template
from holidays.utils import holidays_remaining as holidays_remaining_fn


register = template.Library()


@register.filter
def holidays_remaining(user, year):
    return holidays_remaining_fn(user, year)