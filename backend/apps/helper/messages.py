from django.conf import settings
from mailqueue.models import MailerMessage


def email_reserva(usuario, local):    
    subject = 'Un Usuario A Reservado Su Local'
    message = f'El {usuario.username}, a reservado su local.'
    email_from = settings.EMAIL_HOST_USER
    user_new_email = local.responsable_email
    send = MailerMessage(subject=subject, content=message, from_address=email_from, to_address=user_new_email)
    send.save()


def email_reserva_state(usuario, reservacion):
    if reservacion.estado == "Aprobada":
        subject = 'Su Reservación Fue Aprobada Por El Responsable Del Local'
        message = f'Su Reservación al local: {reservacion.local.nombre} fue aprobada'
        email_from = settings.EMAIL_HOST_USER
        user_new_email = usuario.email
        send = MailerMessage(subject=subject, content=message, from_address=email_from, to_address=user_new_email)
        send.save()
    elif reservacion.estado == "Cancelada":
        subject = 'Su Reservación Fue Cancelada Por El Responsable Del Local'
        message = f'Su Reservación al local: {reservacion.local.nombre} fue cancelada por el motivo:{reservacion.motivo}'
        email_from = settings.EMAIL_HOST_USER
        user_new_email = usuario.email
        send = MailerMessage(subject=subject, content=message, from_address=email_from, to_address=user_new_email)
        send.save()
    else:
        return "reservacion pendiente"
