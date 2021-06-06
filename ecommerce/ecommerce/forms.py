from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                                label= 'Usuario',
                                widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'id': 'username'
                                    }))
    email = forms.EmailField(required=True,
                                widget=forms.EmailInput(
                                    attrs={
                                        'class':'form-control',
                                        'id': 'email',
                                    }))
    password = forms.CharField(required=True, min_length= 8,
                                label='Contraseña',
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class':'form-control',
                                        'id': 'password',
                                    }))
    password2 = forms.CharField(required=True, min_length= 8,
                                label='Confirmar contraseña',
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class':'form-control',
                                        'id': 'password',
                                    }))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario ya se encuentra en uso.')

        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso.')

        return email

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2','La contraseña no coincide.')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )


class LoginForm(forms.Form):
    username = forms.CharField(required=True,
                                label= 'Usuario',
                                widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'id': 'username'
                                    }))
    password = forms.CharField(required=True, min_length= 8,
                                label='Contraseña',
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class':'form-control',
                                        'id': 'password',
                                    }))

    def validate(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        return authenticate(username = username, password = password)


        