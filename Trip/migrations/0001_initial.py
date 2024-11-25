# Generated by Django 4.2 on 2024-11-09 22:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trajet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_depart', models.CharField(max_length=100)),
                ('point_arrivee', models.CharField(max_length=100)),
                ('date_depart', models.DateField()),
                ('heure_depart', models.TimeField()),
                ('prix_par_place', models.DecimalField(decimal_places=2, max_digits=10)),
                ('places_disponibles', models.IntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=4, message='le nombre de place doit etre inférieur ou égale à 4')])),
                ('statut', models.CharField(choices=[('actif', 'Actif'), ('complet', 'Complet'), ('annulé', 'Annulé')], max_length=20)),
                ('conducteur_nom_complet', models.CharField(max_length=200)),
                ('conducteur_contact', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Le contact du conducteur est composé de 8 chiffres.', regex='^\\d{8}$')])),
                ('matricule', models.CharField(max_length=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]