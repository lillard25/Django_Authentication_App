from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username_or_email = forms.CharField(label="Username or Email", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No account found with this email address.")
        return email

