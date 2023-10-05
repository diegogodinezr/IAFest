from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Q
from datetime import datetime, timedelta
# Create your views here.

def filtrosv(request):
    formulario = TablaForm()
    consulta = Tabla.objects.all()
    if request.method == 'GET':
        idc = request.GET.get('id_registrof')
        fechac = request.GET.get('fecha_ingresof')
        fechasc = request.GET.get('fecha_sintomasf')
        edadc = request.GET.get('edadf')
        pais_nacimientoc = request.GET.get('pais_nacimientof')

        if idc:
            consulta = consulta.filter(id_registro=idc)
        if fechac:
            consulta = consulta.filter(fecha_ingreso=fechac)
        if fechasc:
            consulta = consulta.filter(fecha_sintomas=fechasc)
        if edadc:
            consulta = consulta.filter(edad=edadc)
        if pais_nacimientoc:
            consulta = consulta.filter(pais_nacimiento=pais_nacimientoc)

    if not consulta.exists():
        messages.info(request, 'No se encontraron resultados.')

    context = {
        "formulario": formulario,
        "listacovid": consulta,
    }

    return render(request, 'Tabla_cov.html', context)
