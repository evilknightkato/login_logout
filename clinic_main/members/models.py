from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email

# Create your models here.

class CustomUser(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    family_user = models.CharField(max_length=100,blank=True,verbose_name="Фамилия")
    name_user = models.CharField(max_length=100,blank=True,verbose_name='Имя')
    middle_name = models.CharField(max_length=100,blank=True,verbose_name='Отчество')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.username} ({'Персонал' if self.is_doctor else 'Клиент'})"

class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    polis_num = models.CharField(max_length=16)

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
