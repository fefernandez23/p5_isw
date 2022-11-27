from django.contrib.auth.forms import AuthenticationForm
from django import forms
import main_app.models as _


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = _.User
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control form-control-lg '}),
            'apellidos': forms.TextInput(
                attrs={'class': 'form-control form-control-lg '}),
            'ci': forms.TextInput(
                attrs={'class': 'form-control form-control-lg '}),
            'tfno': forms.TextInput(
                attrs={'class': 'form-control form-control-lg '}),
            'apto': forms.TextInput(
                attrs={'class': 'form-control form-control-lg '}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control form-control-lg '}),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control form-control-lg'}),
        }
