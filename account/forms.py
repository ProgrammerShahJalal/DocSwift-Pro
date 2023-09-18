from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import ContactMessage

USER_CHOICES = [
    ('D', 'Doctor'),
    ('P', 'Patient'),
    ('HR', 'HR'),
]

class UserCreateForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=USER_CHOICES, required=True, widget=forms.RadioSelect)
    class Meta:
        fields = ("first_name", "last_name", "username", "email", "password1", "password2", "user_type")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email address"



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        