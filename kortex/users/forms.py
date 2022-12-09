from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from django import forms


class UserSignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "***"}
        ),
    )

    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "***"}
        ),
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "first_name", "last_name")
        widgets = {
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "example@test.com"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "John"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Johnson"}
            ),
        }


class UserSignInForm(AuthenticationForm):
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "***"}
        ),
    )

    username = forms.EmailField(
        label="email",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "example@test.com"}
        ),
    )
