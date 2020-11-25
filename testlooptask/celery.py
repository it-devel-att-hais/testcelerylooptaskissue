import os

import django
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testlooptask.settings')

django.setup()
app = Celery('testlooptask')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'print_hello_world': {
        'task': 'print_hello_world',
        'schedule': crontab(minute='*/1'),  # Executes every minute
    },
}
