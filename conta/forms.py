from django import forms
from .models import Usuario

class SignForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','nome','sobrenome','email','senha']
        widgets = {
            'email' : forms.EmailInput,
            'senha' : forms.PasswordInput,
        }

    r_senha = forms.CharField(label='Repita a senha',max_length=80,widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de usuario (Apelido)',max_length=50)
    senha = forms.CharField(label="Senha",max_length=80,widget=forms.PasswordInput)


