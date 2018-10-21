from __future__ import absolute_import, unicode_literals

import datetime

from celery import shared_task
from django.core.exceptions import ValidationError
from django.http import HttpResponse

from currencies.utils import get_currency_rates_from_api
from currencies.views import rate_model


@shared_task(name='update_currency_rates')
def update_currency_rates():
    one_day_ago = get_datetime_a_day_ago(now=datetime.datetime.now())

    currencies_rates = get_currencies_rates(one_day_ago)

    if not currencies_rates:
        return HttpResponse(status=200)

    for currency_rate in currencies_rates:
        try:
            new_rates = get_currency_rates_from_api(base_currency=currency_rate.from_currency.short_name)

            cost = get_cost(rates=new_rates, currency_short_name=currency_rate.to_currency.short_name)

            currency_rate.cost = cost
            currency_rate.save()
        except (KeyError, TypeError, ValidationError):
            return HttpResponse(status=500)


def get_datetime_a_day_ago(now):
    return now - datetime.timedelta(days=1)


def get_currencies_rates(updated_at):
    # quantity for dev
    return rate_model.objects.filter(updated_at__lt=updated_at)[:3]


def get_cost(rates, currency_short_name):
    cost = rates[currency_short_name]
    return round(cost, 2)
