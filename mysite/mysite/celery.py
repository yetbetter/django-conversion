from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('mysite')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'update-currency-rates-every-5-seconds': {
        'task': 'update_currency_rates',
        # time for dev
        'schedule': 5.0,
    },
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))