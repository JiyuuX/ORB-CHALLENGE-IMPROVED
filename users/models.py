from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
import secrets
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    register_date = models.DateTimeField(default=timezone.now)
    api_key = models.CharField(max_length=255, blank=True)
    api_secret_key = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # Kullanıcının API anahtarlarını oluştur
        if not self.api_key:
            self.api_key = get_random_string(length=32)
        if not self.api_secret_key:
            self.api_secret_key = get_random_string(length=32)

        # Kullanıcıyı kaydet
        super().save(*args, **kwargs)

        # Kullanıcıya e-posta ile API anahtarlarını gönder
        subject = 'API Key and Secret Key'
        message = f'Your API Key: {self.api_key}\nYour API Secret Key: {self.api_secret_key}'
        from_email = settings.EMAIL_HOST_USER
        to_email = self.email
        send_mail(subject, message, from_email, [to_email])


    def generate_api_keys(self):
        self.api_key = secrets.token_hex(16)  # Rastgele 32 karakter uzunluğunda bir dize oluşturur
        self.api_secret_key = secrets.token_urlsafe(32)  # Rastgele 64 karakter uzunluğunda bir dize oluşturur
        self.save()