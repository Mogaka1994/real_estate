# Generated by Django 2.0.5 on 2018-05-30 20:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Property Price')),
                ('description', models.TextField(verbose_name='Property Details')),
                ('location', models.CharField(max_length=200, verbose_name='Property Location')),
                ('sale_type', models.CharField(max_length=100, verbose_name='Type of Sale')),
                ('date_added', models.DateField(default=django.utils.timezone.now, verbose_name='Date Registered')),
                ('bedrooms', models.IntegerField(default=0, verbose_name='Number of Bedrooms')),
                ('kitchens', models.IntegerField(default=0, verbose_name='Number of Kitchens')),
                ('living_rooms', models.IntegerField(default=0, verbose_name='Number of Living Rooms')),
                ('parking', models.IntegerField(default=0, verbose_name='Number of Parking Lots')),
                ('picture_1', models.ImageField(upload_to='property/2018-05-30 20:21:47.915758+00:00')),
                ('picture_2', models.ImageField(null=True, upload_to='property/2018-05-30 20:21:47.915927+00:00')),
                ('picture_3', models.ImageField(null=True, upload_to='property/2018-05-30 20:21:47.915958+00:00')),
                ('picture_4', models.ImageField(null=True, upload_to='property/2018-05-30 20:21:47.915983+00:00')),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='agent.Agent', verbose_name='Agent')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.PropertyType', verbose_name='Property Type'),
        ),
    ]