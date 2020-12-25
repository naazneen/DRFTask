from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import datetime


year_choices = [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

class Aadhar(models.Model):
    AadharNumber = models.CharField(max_length=12,primary_key=True)
    is_Active = models.BooleanField()

class Address(models.Model):
    aadhar = models.ForeignKey(Aadhar,on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.TextField(max_length=6)

class Qualification(models.Model):
    aadhar = models.OneToOneField(
        Aadhar,
        on_delete=models.CASCADE,
    )
    school_name = models.CharField(max_length=500)
    year_passing = models.IntegerField(choices=year_choices, default=current_year)
    percentage = models.IntegerField()

class Bank(models.Model):
    aadhar = models.OneToOneField(
        Aadhar,
        on_delete=models.CASCADE,
    )
    account_number = models.CharField(max_length=12)
    bank_name = models.CharField(max_length=200)
    ifsc_code = models.CharField(max_length=30)


class Personal(models.Model):
    aadhar = models.OneToOneField(
        Aadhar,
        on_delete=models.CASCADE,
    )
    full_name = models.CharField(max_length=500)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=3)

class Contact(models.Model):
    phone_number = models.CharField(max_length=12)
    description = models.CharField(max_length=25)
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)


class Email(models.Model):
    email_address = models.CharField(max_length=12)
    description = models.CharField(max_length=25)
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)


class PastExp(models.Model):
    aadhar = models.ForeignKey(Aadhar,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    job_role = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()





