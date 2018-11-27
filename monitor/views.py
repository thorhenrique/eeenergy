from django.shortcuts import render,redirect,reverse
from conta.auth import get_logged_user
from .models import Dica,Gasto
from .forms import GastoForm
from conta.models import Usuario
from datetime import datetime
from datetime import datetime
import random
# Create your views here.

def index(request):
    kwh = ''
    g_dia = 0
    g_hora = 0
    g_semanal = 0
    msg = ''
    val = 0 
    #verifica se o usuario esta autenticado, caso o contrario, redireciona
    #a pagina de entrar
    if get_logged_user(request) == None:
        return redirect(reverse('conta:entrar'))

    dicas = Dica.objects.latest()
    try:
        gastos = Gasto.objects.filter(usuario__pk=request.session['user_id'])
        msg= 'Seus gastos'

        for gasto in gastos:
            now = datetime.now()
        
            if gasto.data.month == now.month:
                val += gasto.kw
            else:
                continue
        
    except:
        msg = 'Você não possui gastos'
    
    if val != 0:
        g_dia = val/30
        g_hora = (val/30)/24
        g_semanal = val/4
    else:
        msg = 'Você não possui gastos!'


    context = {
        'dica' : dicas,
        'g_hora' : g_hora,
        'g_dia' : g_dia,
        'g_semanal' : g_semanal,   
    }

    return render(request,'monitor/index.html',context)

def dicas(request):
    if get_logged_user(request) == None:
        return redirect(reverse('conta:entrar'))

    latest_dicas = Dica.objects.all().order_by('-pub_data')[:6]
    return render(request,'monitor/dicas.html',{'dicas' : latest_dicas})

def gastos(request):
    if get_logged_user(request) == None:
        return redirect(reverse('conta:entrar'))
    #Variavel a ser preenchida com o erro/sucesso de registro
    gasto_info = ''
    info = ''
    #Pegar duas dicas aleatorias
    dicas_all = Dica.objects.all()
    #media de gastos do usuario

    
    #Ultimo registro feito pelo usuario
    try:
        ultimo_registro = Gasto.objects.filter(usuario__pk=request.session['user_id'])[:1]
    except Gasto.DoesNotExist:
        ultimo_registro = None
    
    if ultimo_registro is not None:
        #A checagem sera semanal
        dia_para_registro = ultimo_registro[0].data.day + 7

        #checar o dia atual, se o dia atual for igual a soma do dia do ultimo
        #registro mais 7, está na hora de fazer outro registro
        if datetime.now().day >= dia_para_registro:
            info = "Está na hora de fazer outro registro, rápido!"


    if request.method == 'POST':
        form_gasto = GastoForm(request.POST)
        if form_gasto.is_valid():
            obj = form_gasto.save(commit=False)
            obj.usuario = Usuario.objects.get(pk=request.session['user_id'])
            obj.save()
            gasto_info = 'Inserido com sucesso!'
    else:
        form_gasto = GastoForm()

    context = {'form_gasto' : form_gasto,'gasto_info' : gasto_info,'ultimo_registro' : ultimo_registro, 'info' : info, }
    return render(request,'monitor/gastos.html',context)

