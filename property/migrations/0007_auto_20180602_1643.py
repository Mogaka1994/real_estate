# Generated by Django 2.0.5 on 2018-06-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20180531_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='picture_1',
            field=models.ImageField(upload_to='media/property/2018-06-02 16:43:54.537353+00:00'),
        ),
        migrations.AlterField(
            model_name='property',
            name='picture_2',
            field=models.ImageField(blank=True, null=True, upload_to='media/property/2018-06-02 16:43:54.537405+00:00'),
        ),
        migrations.AlterField(
            model_name='property',
            name='picture_3',
            field=models.ImageField(blank=True, null=True, upload_to='media/property/2018-06-02 16:43:54.537439+00:00'),
        ),
        migrations.AlterField(
            model_name='property',
            name='picture_4',
            field=models.ImageField(blank=True, null=True, upload_to='media/property/2018-06-02 16:43:54.537467+00:00'),
        ),
    ]
