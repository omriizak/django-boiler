# Generated by Django 2.2.6 on 2020-07-31 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employed',
            name='image',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='notemployed',
            name='image',
            field=models.CharField(max_length=50),
        ),
    ]
