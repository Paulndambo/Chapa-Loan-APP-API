from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

GENDER_CHOICES = (
    ("male", "Male"),
    ("femail", "Female"),
)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True)
    id_number = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    postal_code = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

EDUCATION_LEVELS = (
    ("high_school", "High School"),
    ("university", "University"),
    ("college", "College"),
    ("primary_school", "Primary School"),
)

class Education(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    level = models.CharField(max_length=200)
    institution = models.CharField(max_length=500, blank=True, null=True)
    course_name = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField()
    finish_date = models.DateField(null=True)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.institution

    
class Income(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    mpesa_statement = models.FileField(upload_to="mpesa_statements",null=True, blank=True)
    bank_statement = models.FileField(upload_to="bank_statements", null=True, blank=True)
    proof_of_income = models.FileField(upload_to="income_documents", null=True, blank=True)

    def __str__(self):
        return self.customer.user.username
