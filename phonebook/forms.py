from django import forms
from .models import *

# Form for adding/editing a contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number']

# Form for adding/editing application information
class AppInfoForm(forms.ModelForm):
    class Meta:
        model = AppInfo
        fields = '__all__'

# Form for editing user profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

# Form for user registration
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'

# Form for user login
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
