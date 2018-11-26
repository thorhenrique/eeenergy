from django.db import models
from conta.models import Usuario
from datetime import datetime
# Create your models here.

class Dica(models.Model):
    titulo = models.CharField("Titulo",max_length=50)
    desc = models.TextField("Texto da Dica")
    pub_data = models.DateTimeField("Data de publicacao",default=datetime.now,blank=True)
    curtidas = models.IntegerField("Curtidas",default=0)

    class Meta:
        get_latest_by = 'pub_data'
    def __str__(self):
        return self.titulo


class Gasto(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    data = models.DateField("Data", default=datetime.now)
    gasto = models.FloatField("Gasto em Reais", default=0)
    kw = models.FloatField("Kw's gastos",default=0)

    class Meta:
        get_latest_by = 'data'

    def __str__(self):
        return self.data.strftime("%d %m %y")
