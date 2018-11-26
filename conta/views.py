from django.shortcuts import render,redirect,reverse
from .forms import SignForm,LoginForm
from .models import Usuario
from .auth import * #funcoes para autenticacao
# Create your views here.


def index(request):
    if get_logged_user(request) == None:
        return redirect(reverse('conta:entrar'))
    user = get_logged_user(request)
    return render(request,'conta/index.html',{'user' : user,'nome' : user.nome + user.sobrenome })

def cadastrar(request):
    erro = ''
    if request.method == "POST":
            form = SignForm(request.POST)
            if form.is_valid():
                #Se passar no teste de repetir senha
                if request.POST['senha'] == request.POST['r_senha']:
                    post = form.save(commit=False)
                    #set a senha do usuario
                    post.set_pass(request.POST['senha'])
                    post.save()
                    #redirecionar a pagina para a conta do usuario
                    return redirect(reverse("conta:entrar"))
                else:
                    erro = 'As senhas não batem'
    else:
        form = SignForm()

    #carregamento do template
    context = {'form' : form, 'erro' : erro}
    return render(request,'conta/cadastrar.html',context)

def entrar(request):
    erro = ''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = autenticar(request.POST['username'],request.POST['senha'])
            #checar se o usuario existe
            if user != None:
                login(request,user)
                return redirect(reverse("conta:index"))
            else:
                erro = "O usuario nao existe"
    else:
        form = LoginForm()

    context = {'form' : form,'erro' : erro}
    return render(request,'conta/entrar.html',context)

def sair(request):
    logout(request)
    return redirect(reverse('conta:entrar'))
