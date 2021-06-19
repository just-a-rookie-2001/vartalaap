from enum import unique
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField()
    contact_number = PhoneNumberField(null=False, blank=False, unique=True)
    password = models.CharField(max_length=300)
    last_seen = models.DateTimeField()
    