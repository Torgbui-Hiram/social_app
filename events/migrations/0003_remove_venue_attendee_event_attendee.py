# Generated by Django 4.1 on 2022-08-11 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_venue_attendee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='attendee',
        ),
        migrations.AddField(
            model_name='event',
            name='attendee',
            field=models.ManyToManyField(blank=True, to='events.myclubuser'),
        ),
    ]