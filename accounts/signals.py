# accounts/signals.py
from django.conf import settings
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def send_verification_email(sender, instance, created, **kwargs):
    if created:
        subject = "Welcome to Our ForfreeLetters! Verify Your Email"
        context = {
            "first_name": instance.first_name,
            "verification_link": f"{settings.BASE_URL}/verify/{instance.email}",
        }
        html_message = render_to_string(
            "emails/verification_email.html", context
        )

        email = EmailMessage(
            subject, html_message, settings.EMAIL_HOST_USER, [instance.email]
        )
        email.content_subtype = "html"  # Set the content type to HTML
        email.send()
