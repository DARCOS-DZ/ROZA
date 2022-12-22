# Generated by Django 4.1 on 2022-12-21 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate', '0006_topic_id_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='quantity_1',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='position',
            name='quantity_2',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='position',
            name='quantity_3',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='position',
            name='rose_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='rose_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='rose_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
