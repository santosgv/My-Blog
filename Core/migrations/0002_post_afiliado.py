# Generated by Django 4.2.4 on 2023-11-07 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='afiliado',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
