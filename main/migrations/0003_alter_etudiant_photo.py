# Generated by Django 5.0.6 on 2024-06-05 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_etudiant_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='photo',
            field=models.FileField(upload_to='photos/'),
        ),
    ]
