from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse
from .models import Participante, Conferencista


def index(request):
    return render(request, 'registro/index.html')

def participantes(request):
    if request.method == 'POST': #{
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        twitter = request.POST.get('twitter')

        p = Participante(nombre=nombre, apellido=apellido, correo=correo, twitter=twitter)
        p.save()

        msj = f'El participante {nombre} {apellido} ha sido registrado con éxito.'

        messages.add_message(request, messages.INFO, msj)
    #}
    
    q = request.GET.get('q')

    if q: #{
        data = Participante.objects.filter(nombre__startswith=q).order_by('nombre')
    else:
        data = Participante.objects.all().order_by('nombre')
    #}

    ctx = {
        'participantes': data,
        'q': q
    }

    return render(request, 'registro/participantes.html', ctx)

def eliminar_participante(request, id):
    Participante.objects.get(pk=id).delete()
    return redirect(reverse('participantes'))

def conferencistas(request):
    if request.method == "POST": #{
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        experiencia = request.POST.get('experiencia')

        conferencistas = Conferencista(nombre=nombre,apellido=apellido,experiencia=experiencia)
        conferencistas.save()

        msj = f'Se ha registrado correctamente el conferencistas {nombre} {apellido}'

        messages.add_message(request, messages.INFO, msj)

    #}

    q = request.GET.get('q')

    if q : #{
        conferencistas = Conferencista.objects.filter(nombre__startswith=q).order_by('nombre')
    else :
        conferencistas = Conferencista.objects.all().order_by('nombre')
    #}

    ctx = {
        'conferencistas': conferencistas,
        'q':q,
    }
    return render(request, 'registro/conferencistas.html', ctx)