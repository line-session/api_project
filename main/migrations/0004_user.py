# Generated by Django 5.0.6 on 2024-06-05 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_etudiant_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_user', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('number_user', models.IntegerField(blank=True, null=True)),
                ('photo', models.CharField(blank=True, max_length=255, null=True)),
                ('code_bar', models.CharField(blank=True, max_length=255, null=True)),
                ('heure_connexion', models.DateTimeField()),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]