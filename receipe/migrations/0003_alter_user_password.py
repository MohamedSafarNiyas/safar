# Generated by Django 4.2.4 on 2023-08-18 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipe', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
