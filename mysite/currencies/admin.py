from django.contrib import admin

from currencies.models import Currency, Rate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'country')


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ['from_currency', 'to_currency', 'cost', 'updated_at']

