from django.db import models
#senha
import random,string
from django.contrib.auth.hashers import make_password

# Create your models here.

class Usuario(models.Model):
    username = models.CharField("Apelido do usuario",max_length=50,unique=True)
    nome = models.CharField("Primeiro nome",max_length=50)
    sobrenome = models.CharField("Sobrenome",max_length=50)
    email = models.EmailField("Email",unique=True)
    senha = models.CharField("Senha Encriptada",max_length=80)
    salt = models.CharField("Salt da senha",max_length=16)

    #Funcao para definir a senha do usuario
    def set_pass(self,senha,salt=None):
        if salt == None:
            self.salt = "".join(random.choices(string.ascii_letters+string.digits, k=16))
        else:
            self.salt = str(salt)

        self.senha = make_password(senha,salt=self.salt)
        return

    def cmp_senha(self,senha):
        if make_password(senha,self.salt) == self.senha:
            return True
        else:
            return False

