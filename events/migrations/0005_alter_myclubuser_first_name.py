# Generated by Django 4.1 on 2022-08-18 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myclubuser',
            name='first_name',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='events.venue'),
        ),
    ]
