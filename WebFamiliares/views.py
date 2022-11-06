from django.http import HttpResponse
from django.template import Template, Context, loader

def Familiares(request):
    Integrantes=["Constanza Gonzalez", "Ezequiel Gonzalez", "Hernan Gonzalez", "Carolina Juri"]

    Edades=[19, 25, 53, 54]

    datos={"Edades":Edades, "Integrantes":Integrantes}

    plantilla=loader.get_template("Template.html")

    documento=plantilla.render(datos)

    return HttpResponse(documento)