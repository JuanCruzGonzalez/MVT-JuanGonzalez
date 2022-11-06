from django.shortcuts import render
from django.http import HttpResponse
from familiares.models import Familiar
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def Lista_Familiar(request):
    familiares=Familiar.objects.all()
    num=0
    constanza=""
    for nombre in familiares:
        constanza += nombre.nombre + nombre.apellido+ "|"  + str(nombre.edad)+ "|"  + str(nombre.nacimiento)
        break
    ezequiel=""
    num=0
    for nombre in familiares:
        if num == 1:
            ezequiel += nombre.nombre + nombre.apellido+ "|"  + str(nombre.edad)+ "|"  + str(nombre.nacimiento)
            break
        num=num+1
    carolina=""
    num=0
    for nombre in familiares:
        if num == 3:
            carolina += nombre.nombre + nombre.apellido+ "|"  + str(nombre.edad)+ "|"  + str(nombre.nacimiento)
            break
        num=num+1
    hernan=""
    num=0
    for nombre in familiares:
        if num==2:
            hernan += nombre.nombre + nombre.apellido+ "|"  + str(nombre.edad)+ "|"  + str(nombre.nacimiento)
            break
        num=num+1

    persona={"Constanza":constanza,"Ezequiel": ezequiel, "Hernan":hernan, "Carolina":carolina}
    
    plantilla=loader.get_template("Template.html")

    documento=plantilla.render(persona)

    return HttpResponse(documento)