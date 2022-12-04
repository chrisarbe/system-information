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
    path('proveedores/', views.proveedores, name='proveedores'),
    path('tipo_documento/', views.tipo_documento, name='tipo_documento'),
    path('tipo_documento/agregar/', views.tipo_documento_agregar, name='tipo_documento_agregar'),
    path('tipo_documento/ver/', views.tipo_documento_ver, name='tipo_documento_ver'),
    path('tipo_documento/editar/', views.tipo_documento_editar, name='tipo_documento_editar'),
    path('tipo_documento/borrar/', views.tipo_documento_borrar, name='tipo_documento_borrar'),
]
