# Generated by Django 4.1 on 2022-11-24 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate', '0002_category_flower_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='id_reference',
            field=models.IntegerField(null=True),
        ),
    ]
