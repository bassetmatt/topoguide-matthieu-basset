# Generated by Django 4.0.4 on 2022-04-22 07:46

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itineraires', '0004_alter_sortie_weather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itineraire',
            name='base_height',
            field=models.IntegerField(default=0, verbose_name='Altitude de départ'),
        ),
        migrations.AlterField(
            model_name='itineraire',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='itineraire',
            name='estim_difficulty',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Difficulté estimée'),
        ),
        migrations.AlterField(
            model_name='itineraire',
            name='estim_duration',
            field=models.TimeField(default=datetime.time(1, 0), verbose_name='Durée estimée'),
        ),
        migrations.AlterField(
            model_name='itineraire',
            name='max_height',
            field=models.IntegerField(default=0, verbose_name='Altitude maximale'),
        ),
        migrations.AlterField(
            model_name='itineraire',
            name='min_height',
            field=models.IntegerField(default=0, verbose_name='Altitude minimale'),
        ),
        migrations.AlterField(
            model_name='itineraire',
            name='neg_elev_gain',
            field=models.IntegerField(default=0, verbose_name='Dénivelé cumulé négatif'),
        ),
        migrations.AlterField(
            model_name='itineraire',
            name='pos_elev_gain',
            field=models.IntegerField(default=0, verbose_name='Dénivelé cumulé positif'),
        ),
        migrations.AlterField(
            model_name='itineraire',
            name='start_point',
            field=models.CharField(max_length=100, verbose_name='Point de départ'),
        ),
        migrations.AlterField(
            model_name='itineraire',
            name='title',
            field=models.CharField(max_length=50, verbose_name="Nom de l'itinéraire"),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='actual_duration',
            field=models.TimeField(default=datetime.time(1, 0), verbose_name='Durée réelle'),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date de la sortie'),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='difficulty_felt',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Difficulté ressentie'),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='group_xp',
            field=models.CharField(choices=[('B', 'Tous débutants'), ('E', 'Tous expérimentés'), ('M', 'Mixte')], default='B', max_length=1, verbose_name='Expérience du groupe'),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='number_people',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Nombre de participants'),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itineraires.itineraire', verbose_name='Itinéraire'),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur'),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='weather',
            field=models.CharField(choices=[('G', 'Bonnes'), ('N', 'Moyennes'), ('B', 'Mauvaises')], default='G', max_length=1, verbose_name='Conditions météo'),
        ),
    ]
