import locale

from django import template

register = template.Library()


@register.filter
def sum_transcation_total(goods):
    investments = [good.requested_price for good in goods]
    return sum(investments)


@register.filter
def money_format(price):
    try:
        locale.setlocale(locale.LC_ALL, 'en_NG')
        return locale.currency(price, grouping=True)
    except Exception as e:
        return price
