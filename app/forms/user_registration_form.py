from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import TextInput, PasswordInput, CharField

from app.models.user import User


class UserSignUpForm(UserCreationForm):
    password1 = CharField(
        widget=PasswordInput(
            attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'}),
    )
    password2 = CharField(
        widget=PasswordInput(
            attrs={'class': 'form-control form-control-lg', 'placeholder': 'Confirm Password'}),
    )

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'nid_number')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username'}),
            'phone_number': TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Phone Number'}),
            'nid_number': TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'NID Number'})
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'phone_number')