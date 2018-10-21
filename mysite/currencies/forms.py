from django import forms


class RateForm(forms.Form):
    from_currency = forms.IntegerField()
    to_currency = forms.IntegerField()
    amount = forms.DecimalField()
