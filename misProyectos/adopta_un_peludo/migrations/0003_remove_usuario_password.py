# Generated by Django 4.1.2 on 2024-07-06 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopta_un_peludo', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='password',
        ),
    ]