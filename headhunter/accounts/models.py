from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(max_length=255, blank=False, verbose_name="Email")
    phone = PhoneNumberField(unique=True, blank=False, verbose_name="Номер телефона")
    is_company = models.BooleanField(default=False, verbose_name="Роль")
    image = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Фото профиля')

