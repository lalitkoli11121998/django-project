# Generated by Django 3.1.7 on 2021-03-07 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20210307_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessrecord',
            name='name',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='topic',
            field=models.CharField(max_length=264),
        ),
    ]
