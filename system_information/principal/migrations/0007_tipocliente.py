# Generated by Django 4.1.3 on 2022-12-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_municipio'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]
