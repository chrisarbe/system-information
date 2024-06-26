# Generated by Django 4.1.3 on 2024-05-10 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0014_cliente_fecha_nacimiento_proveedor_fecha_nacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoCorporalAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.FloatField()),
                ('altura', models.FloatField()),
                ('estato', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Lactancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_parto', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RazaAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_celo', models.DateField()),
                ('fecha_inseminacion', models.DateField()),
                ('dosis_seminal', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('estado_corporal_animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.estadocorporalanimal')),
                ('raza_animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.razaanimal')),
                ('tipo_animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.tipoanimal')),
            ],
        ),
    ]
