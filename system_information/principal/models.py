from django.db import models
from datetime import datetime

# Create your models here.
class TipoDocumento(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class TipoProveedor(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class TipoCliente(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Magnitud(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Pais(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    nombre=models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    nombre=models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Unidad(models.Model):
    nombre=models.CharField(max_length=100)
    magnitud = models.ForeignKey(Magnitud, on_delete=models.CASCADE)
    simbolo=models.CharField(max_length=5)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre=models.CharField(max_length=100)
    codigo=models.CharField(max_length=10)
    descripcion=models.CharField(max_length=500)

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    nombre=models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    tipo_proveedor=models.ForeignKey(TipoProveedor, on_delete=models.CASCADE)
    tipo_documento=models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero_documento=models.CharField(max_length=20)
    primer_nombre=models.CharField(max_length=20)
    segundo_nombre=models.CharField(max_length=20)
    primer_apellido=models.CharField(max_length=20)
    segundo_apellido=models.CharField(max_length=20)
    nombre_unico=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField(default=datetime.now)
    celular=models.CharField(max_length=15)
    telefono_fijo=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    pais=models.ForeignKey(Pais, on_delete=models.CASCADE)
    departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio=models.ForeignKey(Municipio, on_delete=models.CASCADE)


class Cliente(models.Model):
    tipo_cliente=models.ForeignKey(TipoCliente, on_delete=models.CASCADE)
    tipo_documento=models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero_documento=models.CharField(max_length=20)
    primer_nombre=models.CharField(max_length=20)
    segundo_nombre=models.CharField(max_length=20)
    primer_apellido=models.CharField(max_length=20)
    segundo_apellido=models.CharField(max_length=20)
    nombre_unico=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField(default=datetime.now)
    celular=models.CharField(max_length=15)
    telefono_fijo=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    pais=models.ForeignKey(Pais, on_delete=models.CASCADE)
    departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio=models.ForeignKey(Municipio, on_delete=models.CASCADE)


class ModuloVencimientos(models.Model):
    referencia=models.CharField(max_length=20)
    fecha_factura=models.DateField()
    fecha_vencimiento=models.DateField()
    proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    importe=models.FloatField()
    estato=models.BooleanField()

    def __str__(self):
        return self.referencia
    
# Dato Maestro
class TipoAnimal(models.Model):
    descripcion=models.CharField(max_length=20)

# Dato Maestro
class RazaAnimal(models.Model):
    descripcion=models.CharField(max_length=20)

# Dato Maestro
class EstadoProductivoAnimal(models.Model):
    descripcion=models.CharField(max_length=20)

class EstadoCorporalAnimal(models.Model):
    peso=models.FloatField()
    altura=models.FloatField()
    estato=models.BooleanField()

class Lactancia(models.Model):
    fecha_parto=models.DateField()

class Servicio(models.Model):
    fecha_celo=models.DateField()
    fecha_inseminacion=models.DateField()
    dosis_seminal=models.FloatField()

class Animal(models.Model):
    tipo_animal=models.ForeignKey(TipoAnimal, on_delete=models.CASCADE)
    raza_animal=models.ForeignKey(RazaAnimal, on_delete=models.CASCADE)
    estado_corporal_animal=models.ForeignKey(EstadoCorporalAnimal, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=20)
    fecha_nacimiento=models.DateField()

    def __str__(self):
        return self.nombre