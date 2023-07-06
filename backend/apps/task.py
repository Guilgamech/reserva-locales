# task.py
from celery import shared_task
from mailqueue.models import MailerMessage, MailerMessageManager


@shared_task(name="enviar_correo")
def enviar_correo():
    # Obtener los correos encolados
    queue = MailerMessage.objects.filter(sent=False)
    if queue.exists():
        # Obtener la instancia del objeto encargado de enviar correos
        MailerMessage.objects.send_queued()
    else:
        print("Todos los correos Enviados")
