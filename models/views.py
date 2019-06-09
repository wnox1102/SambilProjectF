from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from models.models import EntradaCC, Camara, Compra, Tienda
from django.db import models
from django.db.models import Count,Sum
import datetime

# Create your views here.

class Graph(View):
    def get(self,request, *args, **kwargs):
        template_name = 'graph.html'
        q1 = EntradaCC.objects.values('fkcamara__modelo').filter(registroe__range=(datetime.datetime(2019,6,2,12,0,0,0), datetime.datetime(2019,6,2,15,0,0,0)), fkcamara_id=3).count()
        print(q1/31,"is the result") 
        return render(request,template_name, {} )

def get_data(request, *args, **kwargs):
        #querys para  contar las personas por camara 
        q1 = EntradaCC.objects.values('fkcamara__modelo').annotate(cuenta=Count('id'))
        # query para mostrar la cantidad de personas que entraron al centro comercial con y sin telefono
        q2 = EntradaCC.objects.values('id').filter(macadd__isnull=True).count()
        q3 = EntradaCC.objects.values('id').filter(macadd__isnull=False).count()
        # querys para determinar la edad de las personas que entran al centro comercial determinando si tiene o no macAddres
        edad1 = EntradaCC.objects.values('edad').filter(edad__range=(10,20), macadd__isnull=True).count()
        edad2 = EntradaCC.objects.values('edad').filter(edad__range=(10,20), macadd__isnull=False).count()
        edad3 = EntradaCC.objects.values('edad').filter(edad__range=(20,30), macadd__isnull=True).count()
        edad4 = EntradaCC.objects.values('edad').filter(edad__range=(20,30), macadd__isnull=False).count()
        edad5 = EntradaCC.objects.values('edad').filter(edad__range=(30,40), macadd__isnull=True).count()
        edad6 = EntradaCC.objects.values('edad').filter(edad__range=(30,40), macadd__isnull=False).count()
        edad7 = EntradaCC.objects.values('edad').filter(edad__range=(40,50), macadd__isnull=True).count()
        edad8 = EntradaCC.objects.values('edad').filter(edad__range=(40,50), macadd__isnull=False).count()
        edad9 = EntradaCC.objects.values('edad').filter(edad__range=(50,60), macadd__isnull=True).count()
        edad10 = EntradaCC.objects.values('edad').filter(edad__range=(50,60), macadd__isnull=False).count()
        # querys que muestran las tiendas que vende mucho mas [top 5]
        qventas = Compra.objects.values('fktienda_id__nombre').annotate(ventas=Sum('total'))[0:5]

        cuenta = []
        camara = []
        SumVentas = []
        tienda = []
        for l in q1:
            cuenta.append(l['cuenta'])
            camara.append(l['fkcamara__modelo'])
            
        for l in qventas:
                tienda.append(l['fktienda_id__nombre'])
                SumVentas.append(l['ventas'])


        data = {
                "labels": camara,
                "default":cuenta,
                "default2":[q2,q3],
                "labels2":['Personas sin telefono','Personas con telefono'],
                "default3":[edad1,edad3, edad5, edad7,edad9],
                "default4":[edad2,edad4,edad6,edad8,edad10],
                "labels4": tienda,
                "default5": SumVentas,
        }
        return JsonResponse(data)