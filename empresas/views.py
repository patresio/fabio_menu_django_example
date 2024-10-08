from django.shortcuts import render

from empresas.models import Empresa


# Create your views here.
def dropdown(request):
    empresas = Empresa.objects.all()
    context = {"empresas": empresas}
    return render(request, "menu.html", context=context)