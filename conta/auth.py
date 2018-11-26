from .models import Usuario

#Funcoes de autenticacao

#checa se o usuario esta autenticado,caso verdadeiro, o retorna
def get_logged_user(request):
    try:
        if request.session['logged'] == True:
            return Usuario.objects.get(pk=request.session['user_id'])
        else:
            return None
    except:
        return None


#autenticar o usuario
def autenticar(username,senha):

    usuario = Usuario.objects.get(username=username)

    if usuario == None:
        return None

    if usuario.cmp_senha(senha):
        return usuario
    return None

#Fazer login do usuario
def login(request,usuario):
    if usuario != None:
        request.session['logged'] = True
        request.session['user_id'] = usuario.pk
        return True
    else:
        return False
    return False

#Faz logout do usuario
def logout(request):
    try:
        if request.session['logged'] == True:
            request.session['user_id'] = None
            request.session['logged'] = False
            return True
        else:
            return False
    except:
        return False




