from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

#Django form
class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your Email')
    msg = forms.CharField(label='Your Message', widget=forms.Textarea)


#model forms
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'phone', 'place', 'img', 'fl']


class UserregForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

class UserloginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']