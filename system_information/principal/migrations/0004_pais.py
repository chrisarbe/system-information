# Generated by Django 4.1.3 on 2022-12-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_tipoproveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]