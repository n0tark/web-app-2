from django.contrib.auth.models import User
from django.db import models

# Model for storing contacts
class Contact(models.Model):
    name = models.CharField(max_length=255)  # Name of the contact
    phone_number = models.CharField(max_length=20)  # Phone number

    def __str__(self):
        return self.name

# Model for storing application information
class AppInfo(models.Model):
    description = models.TextField()  # Description of the application

    def __str__(self):
        return "App Information: Phone contacts"

# Model for storing login credentials
class Login(models.Model):
    email = models.EmailField(unique=True)  # Email address
    password = models.CharField(max_length=8)  # Password

    def __str__(self):
        return self.email

# Model for storing user registration information
class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Reference to User model
    name = models.CharField(max_length=255)  # Name of the user
    email = models.EmailField(unique=True)  # Email address of the user
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)  # Gender of the user
    date_of_birth = models.DateField()  # Date of birth of the user

    def __str__(self):
        return self.name

# Model for storing user profile information
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Reference to User model
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, null=True, blank=True)  # Gender of the user
    date_of_birth = models.DateField(null=True, blank=True)  # Date of birth of the user

    def __str__(self):
        return self.user.username  # Return the username of the user

#########################################

class UserStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username