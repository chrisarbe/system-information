from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import TipoDocumento
from django.core import serializers


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {
            'title':'Dashboard',
            'subtitle':'Resumen de tu Sistema de Información'
            })
    else:
        return render(request, 'login.html')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'mesage':'Bienvenido',
            'code':'1'
            })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'mesage':'Usuario o Clave no válidos',
                'code':'2'
                })
        else:
            login(request, user)
            return redirect('dashboard')


def signout(request):
    logout(request)
    return redirect('login')


def proveedores(request):
    if request.user.is_authenticated:
        return render(request, 'proveedores.html', {
            'title':'Proveedores',
            'subtitle':'Administración de Proveedores'
        })
    else:
        return render(request, 'login.html')


def tipo_documento(request):
    if request.user.is_authenticated:
        lista = TipoDocumento.objects.all()
        return render(request, 'tipo_documento.html', {
            'title':'Tipo de Documento',
            'subtitle':'Administración de Tipo de Documentos',
            'lista':lista
        })
    else:
        return render(request, 'login.html')


def tipo_documento_agregar(request):
    if request.method == 'GET':
        return render(request, 'tipo_documento.html', {
            'mesage':'Formulario Tipo de Documento',
            'code':'1'
            })
    else:
        try:
            documento = TipoDocumento(nombre=request.POST['nombre'])
            documento.save()
            return JsonResponse({'message' : 'Registro Agregado con Éxito', 'status' : '1'}, status=200)
            """return render(request, 'tipo_documento.html', {
                'mesage':'Guardado con Éxito',
                'code':'2'
                })"""
            #return redirect('/tipo_documento/', {'mesage': 'Registro Guardado con Éxito', 'code':'2'})
        except ValueError:
            return render(request, 'tipo_documento.html', {
                'mesage':'Error',
                'code':'3'
                })



def tipo_documento_ver(request):
    item = TipoDocumento.objects.filter(pk=request.POST['dato'])
    response = serializers.serialize("json", item)
    return HttpResponse(response, content_type='application/json')


def tipo_documento_editar(request):
    if request.method == 'GET':
        return render(request, 'tipo_documento.html', {
            'mesage':'Formulario Tipo de Documento',
            'code':'1'
            })
    else:
        try:
            documento = TipoDocumento.objects.get(pk=request.POST['pk_editar'])
            documento.nombre = request.POST['nombre_editar']
            documento.save()
            #return redirect('/tipo_documento/', {'mesage': 'Registro Actualizado con Éxito', 'code':'2'})
            return JsonResponse({'message' : 'Registro Actualizado con exito', 'status' : '1'}, status=200)
        except ValueError:
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)
            """return render(request, 'tipo_documento.html', {
                'mesage':'Error',
                'code':'3'
                })"""


def tipo_documento_borrar(request):
    try:
        item = TipoDocumento.objects.get(pk=request.POST['dato'])
        item.delete()
        return JsonResponse({'message' : 'Registro eliminado con exito', 'status' : '1'}, status=200)
        #return redirect('/tipo_documento/', {'mesage': 'Registro Borrado con Éxito', 'code':'2'})
    except ValueError:
        return render(request, 'tipo_documento.html', {
                'mesage':'Error',
                'code':'3'
                })