# Generated by Django 3.1.4 on 2020-12-19 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terrenos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frente', models.DecimalField(decimal_places=2, max_digits=20)),
                ('fondo', models.DecimalField(decimal_places=2, max_digits=20)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=20)),
                ('name', models.CharField(max_length=100)),
                ('imagen', models.URLField()),
            ],
        ),
    ]