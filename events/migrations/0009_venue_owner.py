# Generated by Django 4.1 on 2022-09-02 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_myclubuser_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='owner',
            field=models.IntegerField(default=1, verbose_name='Owner ID'),
        ),
    ]
