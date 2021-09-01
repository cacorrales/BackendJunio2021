# Generated by Django 3.2.6 on 2021-09-01 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nombres', 'apellidos'],
            },
        ),
    ]
