# Generated by Django 4.2 on 2024-11-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id_notification', models.AutoField(primary_key=True, serialize=False)),
                ('type_notification', models.CharField(choices=[('info', 'Information'), ('warn', 'Warning'), ('alert', 'Alert'), ('Invitation', 'Invitation'), ('Accept', 'Accept'), ('Decline', 'Decline'), ('Application', 'Application')], max_length=50)),
                ('message', models.TextField()),
                ('status_notification', models.CharField(choices=[('sent', 'Sent'), ('pending', 'Pending'), ('failed', 'Failed')], max_length=50)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
    ]