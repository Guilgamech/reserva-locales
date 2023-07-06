# celery.py

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.setting.local')

app = Celery('config')
app.config_from_object('config.setting.local', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_email-1-seconds': {
        'task': 'enviar_correo',
        'schedule': 1.0,
    },

}