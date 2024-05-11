"""system_information URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from principal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.signout, name='logout'),
    # Tipo de Documento
    path('tipo_documento/', views.tipo_documento, name='tipo_documento'),
    path('tipo_documento/agregar/', views.tipo_documento_agregar, name='tipo_documento_agregar'),
    path('tipo_documento/ver/', views.tipo_documento_ver, name='tipo_documento_ver'),
    path('tipo_documento/editar/', views.tipo_documento_editar, name='tipo_documento_editar'),
    path('tipo_documento/borrar/', views.tipo_documento_borrar, name='tipo_documento_borrar'),
    # Tipo de Proveedor
    path('tipo_proveedor/', views.tipo_proveedor, name='tipo_proveedor'),
    path('tipo_proveedor/agregar/', views.tipo_proveedor_agregar, name='tipo_proveedor_agregar'),
    path('tipo_proveedor/ver/', views.tipo_proveedor_ver, name='tipo_proveedor_ver'),
    path('tipo_proveedor/editar/', views.tipo_proveedor_editar, name='tipo_proveedor_editar'),
    path('tipo_proveedor/borrar/', views.tipo_proveedor_borrar, name='tipo_proveedor_borrar'),
    # Tipo de Cliente
    path('tipo_cliente/', views.tipo_cliente, name='tipo_cliente'),
    path('tipo_cliente/agregar/', views.tipo_cliente_agregar, name='tipo_cliente_agregar'),
    path('tipo_cliente/ver/', views.tipo_cliente_ver, name='tipo_cliente_ver'),
    path('tipo_cliente/editar/', views.tipo_cliente_editar, name='tipo_cliente_editar'),
    path('tipo_cliente/borrar/', views.tipo_cliente_borrar, name='tipo_cliente_borrar'),
    # Magnitud
    path('magnitud/', views.magnitud, name='magnitud'),
    path('magnitud/agregar/', views.magnitud_agregar, name='magnitud_agregar'),
    path('magnitud/ver/', views.magnitud_ver, name='magnitud_ver'),
    path('magnitud/editar/', views.magnitud_editar, name='magnitud_editar'),
    path('magnitud/borrar/', views.magnitud_borrar, name='magnitud_borrar'),
    # Pais
    path('pais/', views.pais, name='pais'),
    path('pais/agregar/', views.pais_agregar, name='pais_agregar'),
    path('pais/ver/', views.pais_ver, name='pais_ver'),
    path('pais/editar/', views.pais_editar, name='pais_editar'),
    path('pais/borrar/', views.pais_borrar, name='pais_borrar'),
    # Departamento
    path('departamento/', views.departamento, name='departamento'),
    path('departamento/agregar/', views.departamento_agregar, name='departamento_agregar'),
    path('departamento/ver/', views.departamento_ver, name='departamento_ver'),
    path('departamento/editar/', views.departamento_editar, name='departamento_editar'),
    path('departamento/borrar/', views.departamento_borrar, name='departamento_borrar'),
    # Municipio
    path('municipio/', views.municipio, name='municipio'),
    path('municipio/agregar/', views.municipio_agregar, name='municipio_agregar'),
    path('municipio/ver/', views.municipio_ver, name='municipio_ver'),
    path('municipio/editar/', views.municipio_editar, name='municipio_editar'),
    path('municipio/borrar/', views.municipio_borrar, name='municipio_borrar'),
    # Unidad
    path('unidad/', views.unidad, name='unidad'),
    path('unidad/agregar/', views.unidad_agregar, name='unidad_agregar'),
    path('unidad/ver/', views.unidad_ver, name='unidad_ver'),
    path('unidad/editar/', views.unidad_editar, name='unidad_editar'),
    path('unidad/borrar/', views.unidad_borrar, name='unidad_borrar'),
    # Categoria
    path('categoria/', views.categoria, name='categoria'),
    path('categoria/agregar/', views.categoria_agregar, name='categoria_agregar'),
    path('categoria/ver/', views.categoria_ver, name='categoria_ver'),
    path('categoria/editar/', views.categoria_editar, name='categoria_editar'),
    path('categoria/borrar/', views.categoria_borrar, name='categoria_borrar'),
    # Marca
    path('marca/', views.marca, name='marca'),
    path('marca/agregar/', views.marca_agregar, name='marca_agregar'),
    path('marca/ver/', views.marca_ver, name='marca_ver'),
    path('marca/editar/', views.marca_editar, name='marca_editar'),
    path('marca/borrar/', views.marca_borrar, name='marca_borrar'),
    # Proveedor
    path('proveedor/', views.proveedor, name='proveedor'),
    path('proveedor/agregar/', views.proveedor_agregar, name='proveedor_agregar'),
    path('proveedor/ver/', views.proveedor_ver, name='proveedor_ver'),
    path('proveedor/editar/', views.proveedor_editar, name='proveedor_editar'),
    path('proveedor/borrar/', views.proveedor_borrar, name='proveedor_borrar'),
    # Documentacion
    path('documentacion/', views.documentacion, name='documentacion'),
    path('documentacion_maestros_tecnico/', views.documentacion_maestros_tecnico, name='documentacion_maestros_tecnico'),
    # Documentacion
    path('administracion_pos_caja/', views.administracion_pos_caja, name='administracion_pos_caja'),
    # Tipo de Documento
    path('tipo_animal/', views.tipo_animal, name='tipo_animal'),
    path('tipo_animal/agregar/', views.tipo_animal_agregar, name='tipo_animal_agregar'),
    path('tipo_animal/ver/', views.tipo_animal_ver, name='tipo_animal_ver'),
    path('tipo_animal/editar/', views.tipo_animal_editar, name='tipo_animal_editar'),
    path('tipo_animal/borrar/', views.tipo_animal_borrar, name='tipo_animal_borrar'),
]
