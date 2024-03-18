from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def create_api_keys(sender, instance, created, **kwargs):
    if created:
        # Kullanıcı oluşturulduğunda API anahtarları oluştur
        instance.generate_api_keys()

        # Kullanıcıya e-posta gönder
        send_mail(
            'API Keys Created',
            'Your API keys have been created.',
            'from@example.com',
            [instance.email],
            fail_silently=False,
        )
