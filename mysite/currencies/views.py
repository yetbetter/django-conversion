from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from currencies.forms import RateForm

from currencies.models import Currency, Rate


class CurrencyListView(ListView):
    model = Currency


def convert(request):
    form = RateForm(request.GET)

    if form.is_valid():
        try:
            currency_rate = get_object_or_404(Rate,
                                              from_currency_id=form.cleaned_data['from_currency'],
                                              to_currency_id=form.cleaned_data['to_currency'])
        except Http404:
            result = {'message': 'not found'}
            status = 404
        else:
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
