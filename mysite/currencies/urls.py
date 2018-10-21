from django.urls import path

from currencies import views
from currencies.views import CurrencyListView

urlpatterns = [
    path('', CurrencyListView.as_view(), name='home'),
    path('currency/convert/', views.convert, name='currency_convert')
]
