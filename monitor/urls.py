from django.urls import path
from . import views

app_name='monitor'

urlpatterns = [
    path('',views.index,name='index'),
    path('dicas',views.dicas,name='dicas'),
    path('gastos',views.gastos,name='gastos'),
]
