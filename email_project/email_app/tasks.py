from celery import shared_task
from django.core.mail import send_mail
from .models import EmailRecord

@shared_task
def send_email_task(recipient, subject, message, sender='from@example.com'):
    """
    Задача Celery для отправки email
    """
    # Отправляем email
    send_mail(
        subject,
        message,
        sender,
        [recipient],
        fail_silently=False,
    )
    
    # Сохраняем запись в базе данных
    EmailRecord.objects.create(
        recipient=recipient,
        subject=subject,
        message=message
    )
    
    return f"Email отправлен на {recipient}"