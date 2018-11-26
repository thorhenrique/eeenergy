from django.urls import path
from . import views

app_name = "conta"
urlpatterns = [
    path('',views.index,name='index'),
    path('cadastrar/',views.cadastrar,name='cadastrar'),
    path('entrar/',views.entrar,name='entrar'),
    path('sair/',views.sair,name='sair'),
]
