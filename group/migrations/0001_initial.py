# Generated by Django 4.2 on 2024-11-17 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carpool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, help_text="Description of the carpool's purpose.")),
                ('rules', models.TextField(blank=True, help_text='Rules for the carpool.')),
            ],
        ),
        migrations.CreateModel(
            name='GroupRideReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateTimeField(auto_now_add=True)),
                ('accept_as_group', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('invited', 'Invited'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='invited', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RideReservationParticipants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('accepted', 'Accepted'), ('declined', 'Declined'), ('pending', 'Pending')], default='pending', max_length=20)),
                ('group_ride_reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.groupridereservation')),
            ],
        ),
    ]
