# Generated by Django 3.1.2 on 2020-10-22 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('existencia', models.IntegerField()),
                ('dimension', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=200)),
                ('lote', models.IntegerField()),
                ('Tipo', models.CharField(max_length=200)),
                ('Fecha', models.DateField(null=True)),
            ],
        ),
    ]
