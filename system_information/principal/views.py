from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import *
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

def tipo_animal(request):
    if request.user.is_authenticated:
        lista = TipoAnimal.objects.all()
        return render(request, 'tipo_animal.html', {
            'title':'Tipo de Animal',
            'subtitle':'Administración de Tipo de Animales',
            'lista':lista
        })
    else:
        return render(request, 'login.html')


def tipo_proveedor(request):
    if request.user.is_authenticated:
        lista = TipoProveedor.objects.all()
        return render(request, 'tipo_proveedor.html', {
            'title':'Tipo de Proveedor',
            'subtitle':'Administración de Tipo de Proveedor',
            'lista':lista
        })
    else:
        return render(request, 'login.html')


def tipo_cliente(request):
    if request.user.is_authenticated:
        lista = TipoCliente.objects.all()
        return render(request, 'tipo_cliente.html', {
            'title':'Tipo de Cliente',
            'subtitle':'Administración de Tipo de Cliente',
            'lista':lista
        })
    else:
        return render(request, 'login.html')


def magnitud(request):
    if request.user.is_authenticated:
        lista = Magnitud.objects.all()
        return render(request, 'magnitud.html', {
            'title':'Magnitud',
            'subtitle':'Administración de Magnitudes',
            'lista':lista
        })
    else:
        return render(request, 'login.html')


def pais(request):
    if request.user.is_authenticated:
        lista = Pais.objects.all()
        return render(request, 'pais.html', {
            'title':'País',
            'subtitle':'Administración de Paises',
            'lista':lista
        })
    else:
        return render(request, 'login.html')


def departamento(request):
    if request.user.is_authenticated:
        lista = Departamento.objects.all()
        paises = Pais.objects.all()
        print(paises)
        return render(request, 'departamento.html', {
            'title':'Departamento',
            'subtitle':'Administración de Departamentos',
            'lista':lista,
            'paises':paises
        })
        #response = serializers.serialize("json", paises)
        #return HttpResponse(response, content_type='application/json')
    else:
        return render(request, 'login.html')


def municipio(request):
    if request.user.is_authenticated:
        lista = Municipio.objects.all()
        departamentos = Departamento.objects.all()
        return render(request, 'municipio.html', {
            'title':'Municipio',
            'subtitle':'Administración de Municipios',
            'lista':lista,
            'departamentos':departamentos
        })
    else:
        return render(request, 'login.html')


def unidad(request):
    if request.user.is_authenticated:
        lista = Unidad.objects.all()
        magnitudes = Magnitud.objects.all()
        return render(request, 'unidad.html', {
            'title':'Unidad',
            'subtitle':'Administración de Unidades',
            'lista':lista,
            'magnitudes':magnitudes
        })
    else:
        return render(request, 'login.html')


def categoria(request):
    if request.user.is_authenticated:
        lista = Categoria.objects.all()
        return render(request, 'categoria.html', {
            'title':'Categoría',
            'subtitle':'Administración de Categorias',
            'lista':lista
        })
    else:
        return render(request, 'login.html')


def marca(request):
    if request.user.is_authenticated:
        lista = Marca.objects.all()
        categorias = Categoria.objects.all()
        return render(request, 'marca.html', {
            'title':'Marca',
            'subtitle':'Administración de Marcas',
            'lista':lista,
            'categorias':categorias
        })
    else:
        return render(request, 'login.html')


def proveedor(request):
    if request.user.is_authenticated:
        lista = Proveedor.objects.all()
        tipos_proveedor = TipoProveedor.objects.all()
        tipos_documento = TipoDocumento.objects.all()
        paises = Pais.objects.all()
        departamentos = Departamento.objects.all()
        municipios = Municipio.objects.all()
        return render(request, 'proveedor.html', {
            'title':'Proveedor',
            'subtitle':'Administración de Proveedores',
            'lista':lista,
            'tipos_proveedor':tipos_proveedor,
            'tipos_documento':tipos_documento,
            'paises':paises,
            'departamentos':departamentos,
            'municipios':municipios
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
            nombre_validar = TipoDocumento.objects.filter(nombre=request.POST['nombre'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Documento: ' + str(request.POST['nombre']), 'status' : '0'}, status=200)
            else:
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

def tipo_animal_agregar(request):
    if request.method == 'GET':
        return render(request, 'tipo_animal.html', {
            'mesage':'Formulario Tipo de Animal',
            'code':'1'
            })
    else:
        try:
            descripcion_validar = TipoAnimal.objects.filter(descripcion=request.POST['descripcion'])
            if descripcion_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el descripcion de Animal: ' + str(request.POST['descripcion']), 'status' : '0'}, status=200)
            else:
                animal = TipoAnimal(descripcion=request.POST['descripcion'])
                animal.save()
                return JsonResponse({'message' : 'Registro Agregado con Éxito', 'status' : '1'}, status=200)
        except ValueError:
            return render(request, 'tipo_animal.html', {
                'mesage':'Error',
                'code':'3'
                })

def tipo_proveedor_agregar(request):
    if request.method == 'GET':
        return render(request, 'tipo_proveedor.html', {
            'mesage':'Formulario Tipo de Proveedor',
            'code':'1'
            })
    else:
        try:
            nombre_validar = TipoProveedor.objects.filter(nombre=request.POST['nombre'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Proveedor: ' + str(request.POST['nombre']), 'status' : '0'}, status=200)
            else:
                documento = TipoProveedor(nombre=request.POST['nombre'])
                documento.save()
                return JsonResponse({'message' : 'Registro Agregado con Éxito', 'status' : '1'}, status=200)
        except ValueError:
            return render(request, 'tipo_proveedor.html', {
                'mesage':'Error',
                'code':'3'
                })


def tipo_cliente_agregar(request):
    if request.method == 'GET':
        return render(request, 'tipo_cliente.html', {
            'mesage':'Formulario Tipo de Cliente',
            'code':'1'
            })
    else:
        try:
            nombre_validar = TipoCliente.objects.filter(nombre=request.POST['nombre'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Cliente: ' + str(request.POST['nombre']), 'status' : '0'}, status=200)
            else:
                documento = TipoCliente(nombre=request.POST['nombre'])
                documento.save()
                return JsonResponse({'message' : 'Registro Agregado con Éxito', 'status' : '1'}, status=200)
        except ValueError:
            return render(request, 'tipo_cliente.html', {
                'mesage':'Error',
                'code':'3'
                })


def magnitud_agregar(request):
    if request.method == 'GET':
        return render(request, 'magnitud.html', {
            'mesage':'Formulario Magnitud',
            'code':'1'
            })
    else:
        try:
            nombre_validar = Magnitud.objects.filter(nombre=request.POST['nombre'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Magnitud: ' + str(request.POST['nombre']), 'status' : '0'}, status=200)
            else:
                documento = Magnitud(nombre=request.POST['nombre'])
                documento.save()
                return JsonResponse({'message' : 'Registro Agregado con Éxito', 'status' : '1'}, status=200)
        except ValueError:
            return render(request, 'magnitud.html', {
                'mesage':'Error',
                'code':'3'
                })


def pais_agregar(request):
    if request.method == 'GET':
        return render(request, 'pais.html', {
            'mesage':'Formulario Pais',
            'code':'1'
            })
    else:
        try:
            nombre_validar = Pais.objects.filter(nombre=request.POST['nombre'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Pais: ' + str(request.POST['nombre']), 'status' : '0'}, status=200)
            
            else:
                documento = Pais(nombre=request.POST['nombre'])
                documento.save()
                return JsonResponse({'message' : 'Registro Agregado con Éxito', 'status' : '1'}, status=200)
        except ValueError:
            return render(request, 'pais.html', {
                'mesage':'Error',
                'code':'3'
                })


def departamento_agregar(request):
    if request.method == 'GET':
        return render(request, 'departamento.html', {
            'mesage':'Formulario Pais',
            'code':'1'
            })
    else:
        print("Este es ")
        print(dict(request.POST))
        try:
            nombre_validar = Departamento.objects.filter(nombre=request.POST['nombre'], pais=request.POST['pais'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Departamento: ' + str(request.POST['nombre']), 'status' : '0'}, status=200)
            else:
                documento = Departamento()
                documento.nombre = request.POST['nombre']
                documento.pais = Pais.objects.get(pk = request.POST['pais'])
                documento.save()
                return JsonResponse({'message' : 'Registro Agregado con Éxito', 'status' : '1'}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)


def municipio_agregar(request):
    if request.method == 'GET':
        return render(request, 'municipio.html', {
            'mesage':'Formulario Municipio',
            'code':'1'
            })
    else:
        try:
            nombre_validar = Municipio.objects.filter(nombre=request.POST['nombre'], departamento=request.POST['departamento'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Municipio: ' + str(request.POST['nombre']), 'status' : '0'}, status=200)
            else:
                documento = Municipio()
                documento.nombre = request.POST['nombre']
                documento.departamento = Departamento.objects.get(pk = request.POST['departamento'])
                documento.save()
                return JsonResponse({'message' : 'Registro Agregado con Éxito', 'status' : '1'}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)


def unidad_agregar(request):
    if request.method == 'GET':
        return render(request, 'unidad.html', {
            'mesage':'Formulario Unidad',
            'code':'1'
            })
    else:
        try:
            nombre_validar = Unidad.objects.filter(nombre=request.POST['nombre'], magnitud=request.POST['magnitud'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Unidad: ' + str(request.POST['nombre']), 'status' : '0'}, status=200)
            else:
                documento = Unidad()
                documento.nombre = request.POST['nombre']
                documento.magnitud = Magnitud.objects.get(pk = request.POST['magnitud'])
                documento.simbolo = request.POST['simbolo']
                documento.save()
                return JsonResponse({'message' : 'Registro Agregado con Éxito', 'status' : '1'}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)


def categoria_agregar(request):
    if request.method == 'GET':
        return render(request, 'categoria.html', {
            'mesage':'Formulario Categoría',
            'code':'1'
            })
    else:
        try:
            nombre_validar = Categoria.objects.filter(nombre=request.POST['nombre'], codigo=request.POST['codigo'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Categoría: ' + str(request.POST['nombre']), 'status' : '0'}, status=200)
            else:
                documento = Categoria()
                documento.nombre = request.POST['nombre']
                documento.codigo = request.POST['codigo']
                documento.descripcion = request.POST['descripcion']
                documento.save()
                return JsonResponse({'message' : 'Registro Agregado con Éxito', 'status' : '1'}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)


def marca_agregar(request):
    if request.method == 'GET':
        return render(request, 'marca.html', {
            'mesage':'Formulario Marca',
            'code':'1'
            })
    else:
        try:
            nombre_validar = Marca.objects.filter(nombre=request.POST['nombre'], categoria=request.POST['categoria'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Marca: ' + str(request.POST['nombre']), 'status' : '0'}, status=200)
            else:
                documento = Marca()
                documento.nombre = request.POST['nombre']
                documento.categoria = Categoria.objects.get(pk = request.POST['categoria'])
                documento.save()
                return JsonResponse({'message' : 'Registro Agregado con Éxito', 'status' : '1'}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)


def proveedor_agregar(request):
    if request.method == 'GET':
        return render(request, 'proveedor.html', {
            'mesage':'Formulario Proveedor',
            'code':'1'
            })
    else:
        try:
            nombre_validar = Proveedor.objects.filter(numero_documento=request.POST['numero_documento'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el numero de documento de Proveedor: ' + str(request.POST['numero_documento']), 'status' : '0'}, status=200)
            else:
                documento = Proveedor()
                documento.tipo_proveedor = TipoProveedor.objects.get(pk = request.POST['tipo_proveedor'])
                documento.tipo_documento = TipoDocumento.objects.get(pk = request.POST['tipo_documento'])
                documento.numero_documento = request.POST['numero_documento']
                documento.primer_nombre = request.POST['primer_nombre']
                documento.segundo_nombre = request.POST['segundo_nombre']
                documento.primer_apellido = request.POST['primer_apellido']
                documento.segundo_apellido = request.POST['segundo_apellido']
                documento.celular = request.POST['celular']
                #documento.fijo = request.POST['nombre']
                documento.email = request.POST['email']
                documento.direccion = request.POST['direccion']
                documento.pais = Pais.objects.get(pk = request.POST['pais'])
                documento.departamento = Departamento.objects.get(pk = request.POST['departamento'])
                documento.municipio = Municipio.objects.get(pk = request.POST['municipio'])
                #documento.codigo_postal = request.POST['nombre']
                #documento.numero_impuesto = request.POST['nombre']
                #documento.saldo = request.POST['nombre']
                #documento.termino_pago = request.POST['nombre']
                documento.save()
                return JsonResponse({'message' : 'Registro Agregado con Éxito', 'status' : '1'}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)



def tipo_documento_ver(request):
    item = TipoDocumento.objects.filter(pk=request.POST['dato'])
    response = serializers.serialize("json", item)
    return HttpResponse(response, content_type='application/json')

def tipo_animal_ver(request):
    item = TipoAnimal.objects.filter(pk=request.POST['dato'])
    response = serializers.serialize("json", item)
    return HttpResponse(response, content_type='application/json')

def tipo_proveedor_ver(request):
    item = TipoProveedor.objects.filter(pk=request.POST['dato'])
    response = serializers.serialize("json", item)
    return HttpResponse(response, content_type='application/json')

def tipo_cliente_ver(request):
    item = TipoCliente.objects.filter(pk=request.POST['dato'])
    response = serializers.serialize("json", item)
    return HttpResponse(response, content_type='application/json')

def magnitud_ver(request):
    item = Magnitud.objects.filter(pk=request.POST['dato'])
    response = serializers.serialize("json", item)
    return HttpResponse(response, content_type='application/json')

def pais_ver(request):
    item = Pais.objects.filter(pk=request.POST['dato'])
    response = serializers.serialize("json", item)
    return HttpResponse(response, content_type='application/json')

def departamento_ver(request):
    item = Departamento.objects.filter(pk=request.POST['dato'])
    response = serializers.serialize("json", item)
    return HttpResponse(response, content_type='application/json')

def municipio_ver(request):
    item = Municipio.objects.filter(pk=request.POST['dato'])
    response = serializers.serialize("json", item)
    return HttpResponse(response, content_type='application/json')

def unidad_ver(request):
    item = Unidad.objects.filter(pk=request.POST['dato'])
    response = serializers.serialize("json", item)
    return HttpResponse(response, content_type='application/json')

def categoria_ver(request):
    item = Categoria.objects.filter(pk=request.POST['dato'])
    response = serializers.serialize("json", item)
    return HttpResponse(response, content_type='application/json')

def marca_ver(request):
    item = Marca.objects.filter(pk=request.POST['dato'])
    response = serializers.serialize("json", item)
    return HttpResponse(response, content_type='application/json')

def proveedor_ver(request):
    item = Proveedor.objects.filter(pk=request.POST['dato'])
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
            nombre_validar = TipoDocumento.objects.filter(nombre=request.POST['nombre_editar'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Documento: ' + str(request.POST['nombre_editar']), 'status' : '0'}, status=200)
            else:
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

def tipo_animal_editar(request):
    if request.method == 'GET':
        return render(request, 'tipo_animal.html', {
            'mesage':'Formulario Tipo de Animal',
            'code':'1'
            })
    else:
        try:
            descripcion_validar = TipoAnimal.objects.filter(descripcion=request.POST['descripcion_editar'])
            if descripcion_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Animal: ' + str(request.POST['descripcion_editar']), 'status' : '0'}, status=200)
            else:
                animal = TipoAnimal.objects.get(pk=request.POST['pk_editar'])
                animal.descripcion = request.POST['descripcion_editar']
                animal.save()
                #return redirect('/tipo_documento/', {'mesage': 'Registro Actualizado con Éxito', 'code':'2'})
                return JsonResponse({'message' : 'Registro Actualizado con exito', 'status' : '1'}, status=200)
        except ValueError:
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)

def tipo_proveedor_editar(request):
    if request.method == 'GET':
        return render(request, 'tipo_proveedor.html', {
            'mesage':'Formulario Tipo de Proveedor',
            'code':'1'
            })
    else:
        try:
            nombre_validar = TipoProveedor.objects.filter(nombre=request.POST['nombre_editar'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Proveedor: ' + str(request.POST['nombre_editar']), 'status' : '0'}, status=200)
            else:
                documento = TipoProveedor.objects.get(pk=request.POST['pk_editar'])
                documento.nombre = request.POST['nombre_editar']
                documento.save()
                return JsonResponse({'message' : 'Registro Actualizado con exito', 'status' : '1'}, status=200)
        except ValueError:
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)


def tipo_cliente_editar(request):
    if request.method == 'GET':
        return render(request, 'tipo_cliente.html', {
            'mesage':'Formulario Tipo de Cliente',
            'code':'1'
            })
    else:
        try:
            nombre_validar = TipoCliente.objects.filter(nombre=request.POST['nombre_editar'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Cliente: ' + str(request.POST['nombre_editar']), 'status' : '0'}, status=200)
            else:
                documento = TipoCliente.objects.get(pk=request.POST['pk_editar'])
                documento.nombre = request.POST['nombre_editar']
                documento.save()
                return JsonResponse({'message' : 'Registro Actualizado con exito', 'status' : '1'}, status=200)
        except ValueError:
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)


def magnitud_editar(request):
    if request.method == 'GET':
        return render(request, 'magnitud.html', {
            'mesage':'Formulario Magnitud',
            'code':'1'
            })
    else:
        try:
            nombre_validar = Magnitud.objects.filter(nombre=request.POST['nombre_editar'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Magnitud: ' + str(request.POST['nombre_editar']), 'status' : '0'}, status=200)
            else:
                documento = Magnitud.objects.get(pk=request.POST['pk_editar'])
                documento.nombre = request.POST['nombre_editar']
                documento.save()
                return JsonResponse({'message' : 'Registro Actualizado con exito', 'status' : '1'}, status=200)
        except ValueError:
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)


def pais_editar(request):
    if request.method == 'GET':
        return render(request, 'pais.html', {
            'mesage':'Formulario Pais',
            'code':'1'
            })
    else:
        try:
            nombre_validar = Pais.objects.filter(nombre=request.POST['nombre_editar'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Pais: ' + str(request.POST['nombre_editar']), 'status' : '0'}, status=200)
            else:
                documento = Pais.objects.get(pk=request.POST['pk_editar'])
                documento.nombre = request.POST['nombre_editar']
                documento.save()
                return JsonResponse({'message' : 'Registro Actualizado con exito', 'status' : '1'}, status=200)
        except ValueError:
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)


def departamento_editar(request):
    if request.method == 'GET':
        return render(request, 'departamento.html', {
            'mesage':'Formulario Departamento',
            'code':'1'
            })
    else:
        try:
            nombre_validar = Departamento.objects.filter(nombre=request.POST['nombre_editar'], pais=request.POST['pais_editar'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Departamento: ' + str(request.POST['nombre_editar']), 'status' : '0'}, status=200)
            else:
                documento = Departamento.objects.get(pk=request.POST['pk_editar'])
                documento.nombre = request.POST['nombre_editar']
                documento.pais = Pais.objects.get(pk = request.POST['pais_editar'])
                documento.save()
                return JsonResponse({'message' : 'Registro Actualizado con exito', 'status' : '1'}, status=200)
        except ValueError:
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)


def municipio_editar(request):
    if request.method == 'GET':
        return render(request, 'municipio.html', {
            'mesage':'Formulario Municipio',
            'code':'1'
            })
    else:
        try:
            nombre_validar = Municipio.objects.filter(nombre=request.POST['nombre_editar'], departamento=request.POST['departamento_editar'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Municipio: ' + str(request.POST['nombre_editar']), 'status' : '0'}, status=200)
            else:
                documento = Municipio.objects.get(pk=request.POST['pk_editar'])
                documento.nombre = request.POST['nombre_editar']
                documento.departamento = Departamento.objects.get(pk = request.POST['departamento_editar'])
                documento.save()
                return JsonResponse({'message' : 'Registro Actualizado con exito', 'status' : '1'}, status=200)
        except ValueError:
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)


def unidad_editar(request):
    if request.method == 'GET':
        return render(request, 'unidad.html', {
            'mesage':'Formulario Unidad',
            'code':'1'
            })
    else:
        try:
            nombre_validar = Unidad.objects.filter(nombre=request.POST['nombre_editar'], magnitud=request.POST['magnitud_editar'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Unidad: ' + str(request.POST['nombre_editar']), 'status' : '0'}, status=200)
            else:
                documento = Unidad.objects.get(pk=request.POST['pk_editar'])
                documento.nombre = request.POST['nombre_editar']
                documento.magnitud = Magnitud.objects.get(pk = request.POST['magnitud_editar'])
                documento.simbolo = request.POST['simbolo_editar']
                documento.save()
                return JsonResponse({'message' : 'Registro Actualizado con exito', 'status' : '1'}, status=200)
        except ValueError:
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)


def categoria_editar(request):
    if request.method == 'GET':
        return render(request, 'categoria.html', {
            'mesage':'Formulario Categoría',
            'code':'1'
            })
    else:
        try:
            nombre_validar = Categoria.objects.filter(nombre=request.POST['nombre_editar'], codigo=request.POST['codigo_editar'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Categoría: ' + str(request.POST['nombre_editar']), 'status' : '0'}, status=200)
            else:
                documento = Categoria.objects.get(pk=request.POST['pk_editar'])
                documento.nombre = request.POST['nombre_editar']
                documento.codigo = request.POST['codigo_editar']
                documento.descripcion = request.POST['descripcion_editar']
                documento.save()
                return JsonResponse({'message' : 'Registro Actualizado con exito', 'status' : '1'}, status=200)
        except ValueError:
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)


def marca_editar(request):
    if request.method == 'GET':
        return render(request, 'marca.html', {
            'mesage':'Formulario Marca',
            'code':'1'
            })
    else:
        try:
            nombre_validar = Marca.objects.filter(nombre=request.POST['nombre_editar'], categoria=request.POST['categoria_editar'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el nombre de Marca: ' + str(request.POST['nombre_editar']), 'status' : '0'}, status=200)
            else:
                documento = Marca.objects.get(pk=request.POST['pk_editar'])
                documento.nombre = request.POST['nombre_editar']
                documento.categoria = Categoria.objects.get(pk = request.POST['categoria_editar'])
                documento.save()
                return JsonResponse({'message' : 'Registro Actualizado con exito', 'status' : '1'}, status=200)
        except ValueError:
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)


def proveedor_editar(request):
    if request.method == 'GET':
        return render(request, 'proveedor.html', {
            'mesage':'Formulario Proveedor',
            'code':'1'
            })
    else:
        try:
            nombre_validar = Proveedor.objects.filter(numero_documento=request.POST['numero_documento_editar'])
            if nombre_validar.exists():
                return JsonResponse({'message' : 'Ya existe un registro con el Número Documento de Proveedor: ' + str(request.POST['numero_documento_editar']), 'status' : '0'}, status=200)
            else:
                documento = Proveedor.objects.get(pk=request.POST['pk_editar'])
                documento.tipo_proveedor = TipoProveedor.objects.get(pk = request.POST['tipo_proveedor_editar'])
                documento.tipo_documento = TipoDocumento.objects.get(pk = request.POST['tipo_documento_editar'])
                documento.numero_documento = request.POST['numero_documento_editar']
                documento.primer_nombre = request.POST['primer_nombre_editar']
                documento.segundo_nombre = request.POST['segundo_nombre_editar']
                documento.primer_apellido = request.POST['primer_apellido_editar']
                documento.segundo_apellido = request.POST['segundo_apellido_editar']
                documento.celular = request.POST['celular_editar']
                #documento.fijo = request.POST['nombre']
                documento.email = request.POST['email_editar']
                documento.direccion = request.POST['direccion_editar']
                documento.pais = Pais.objects.get(pk = request.POST['pais_editar'])
                documento.departamento = Departamento.objects.get(pk = request.POST['departamento_editar'])
                documento.municipio = Municipio.objects.get(pk = request.POST['municipio_editar'])
                #documento.codigo_postal = request.POST['nombre']
                #documento.numero_impuesto = request.POST['nombre']
                #documento.saldo = request.POST['nombre']
                #documento.termino_pago = request.POST['nombre']
                documento.save()
                return JsonResponse({'message' : 'Registro Actualizado con exito', 'status' : '1'}, status=200)
        except ValueError:
            return JsonResponse({'message' : 'Error', 'status' : '2'}, status=200)


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

def tipo_animal_borrar(request):
    try:
        item = TipoAnimal.objects.get(pk=request.POST['dato'])
        item.delete()
        return JsonResponse({'message' : 'Registro eliminado con exito', 'status' : '1'}, status=200)
        #return redirect('/tipo_documento/', {'mesage': 'Registro Borrado con Éxito', 'code':'2'})
    except ValueError:
        return render(request, 'tipo_animal.html', {
                'mesage':'Error',
                'code':'3'
                })

def tipo_proveedor_borrar(request):
    try:
        item = TipoProveedor.objects.get(pk=request.POST['dato'])
        item.delete()
        return JsonResponse({'message' : 'Registro eliminado con exito', 'status' : '1'}, status=200)
    except ValueError:
        return render(request, 'tipo_proveedor.html', {
                'mesage':'Error',
                'code':'3'
                })


def tipo_cliente_borrar(request):
    try:
        item = TipoCliente.objects.get(pk=request.POST['dato'])
        item.delete()
        return JsonResponse({'message' : 'Registro eliminado con exito', 'status' : '1'}, status=200)
    except ValueError:
        return render(request, 'tipo_cliente.html', {
                'mesage':'Error',
                'code':'3'
                })


def magnitud_borrar(request):
    try:
        item = Magnitud.objects.get(pk=request.POST['dato'])
        item.delete()
        return JsonResponse({'message' : 'Registro eliminado con exito', 'status' : '1'}, status=200)
    except ValueError:
        return render(request, 'magnitud.html', {
                'mesage':'Error',
                'code':'3'
                })


def pais_borrar(request):
    try:
        item = Pais.objects.get(pk=request.POST['dato'])
        item.delete()
        return JsonResponse({'message' : 'Registro eliminado con exito', 'status' : '1'}, status=200)
    except ValueError:
        return render(request, 'pais.html', {
                'mesage':'Error',
                'code':'3'
                })


def departamento_borrar(request):
    try:
        item = Departamento.objects.get(pk=request.POST['dato'])
        item.delete()
        return JsonResponse({'message' : 'Registro eliminado con exito', 'status' : '1'}, status=200)
    except ValueError:
        return render(request, 'departamento.html', {
                'mesage':'Error',
                'code':'3'
                })

def municipio_borrar(request):
    try:
        item = Municipio.objects.get(pk=request.POST['dato'])
        item.delete()
        return JsonResponse({'message' : 'Registro eliminado con exito', 'status' : '1'}, status=200)
    except ValueError:
        return render(request, 'municipio.html', {
                'mesage':'Error',
                'code':'3'
                })


def unidad_borrar(request):
    try:
        item = Unidad.objects.get(pk=request.POST['dato'])
        item.delete()
        return JsonResponse({'message' : 'Registro eliminado con exito', 'status' : '1'}, status=200)
    except ValueError:
        return render(request, 'unidad.html', {
                'mesage':'Error',
                'code':'3'
                })


def categoria_borrar(request):
    try:
        item = Categoria.objects.get(pk=request.POST['dato'])
        item.delete()
        return JsonResponse({'message' : 'Registro eliminado con exito', 'status' : '1'}, status=200)
    except ValueError:
        return render(request, 'categoria.html', {
                'mesage':'Error',
                'code':'3'
                })


def marca_borrar(request):
    try:
        item = Marca.objects.get(pk=request.POST['dato'])
        item.delete()
        return JsonResponse({'message' : 'Registro eliminado con exito', 'status' : '1'}, status=200)
    except ValueError:
        return render(request, 'marca.html', {
                'mesage':'Error',
                'code':'3'
                })


def proveedor_borrar(request):
    try:
        item = Proveedor.objects.get(pk=request.POST['dato'])
        item.delete()
        return JsonResponse({'message' : 'Registro eliminado con exito', 'status' : '1'}, status=200)
    except ValueError:
        return render(request, 'proveedor.html', {
                'mesage':'Error',
                'code':'3'
                })


def documentacion(request):
    if request.user.is_authenticated:
        return render(request, 'documentacion_navs.html', {
            'title':'Doocumentación',
            'subtitle':'Documentación de la Plataforma'
        })
    else:
        return render(request, 'login.html')


def documentacion_maestros_tecnico(request):
    if request.user.is_authenticated:
        return render(request, 'documentacion_maestros_tecnico.html', {
            'title':'Doocumentación',
            'subtitle':'Documentación de la Plataforma'
        })
    else:
        return render(request, 'login.html')


def administracion_pos_caja(request):
    if request.user.is_authenticated:
        return render(request, 'administracion_pos_caja.html', {
            'title':'Caja',
            'subtitle':'Registro de Compras'
        })
    else:
        return render(request, 'login.html')