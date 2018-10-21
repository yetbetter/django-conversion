from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from currencies.forms import RateForm

from currencies.models import Currency, Rate

rate_model = Rate
currency_model = Currency


class CurrencyListView(ListView):
    model = currency_model


def convert(request):
    form = RateForm(request.GET)

    if form.is_valid():
        currency_rate = get_object_or_404(rate_model,
                                          from_currency_id=form.cleaned_data['from_currency'],
                                          to_currency_id=form.cleaned_data['to_currency'])

        result = {
            'number_of_money': count_money(amount=form.cleaned_data['amount'],
                                           cost=currency_rate.cost)
        }
        status = 200
    else:
        result = form.errors
        status = 400

    return JsonResponse(result, status=status)


def count_money(amount, cost):
    result = amount * cost
    return round(result, 2)
