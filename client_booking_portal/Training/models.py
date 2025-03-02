from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class UserType(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',"password"]

    def __str__(self):
        return self.email

class Client(models.Model):
    address = models.CharField(max_length=500)
    account_details = models.ForeignKey(UserType, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.PositiveIntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])


class Trainer(models.Model):
    address = models.CharField(max_length=500)
    account_details = models.ForeignKey(UserType, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.PositiveIntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])

    
class Course(models.Model):
    name = models.CharField(max_length=300)
    desc = models.TextField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    enrollee = models.ManyToManyField(UserType)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()

    num_of_enrollees = models.IntegerField(default=0)


    def __str__(self):
        return self.name
    
    def add_enrollee(self,user):
        self.num_of_enrollees+= 1
        return self.enrollee.add(user)
    
    @property
    def get_enrollees(self):
        return [enrollee_data.email for enrollee_data in self.enrollee.all()]
