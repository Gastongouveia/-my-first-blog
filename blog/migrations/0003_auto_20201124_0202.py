# Generated by Django 2.2.17 on 2020-11-24 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='situacao',
            field=models.CharField(default='ativo', max_length=7),
        ),
    ]
