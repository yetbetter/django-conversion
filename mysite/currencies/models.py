from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=3, db_index=True)
    country = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.short_name


class Rate(models.Model):
    from_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='from_currency')
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='to_currency')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)
