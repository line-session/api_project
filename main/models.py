from django.db import models

# Create your models here.
class User(models.Model):
    nom_user = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    number_user = models.IntegerField(blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    code_bar = models.CharField(max_length=255, blank=True, null=True)
    heure_connexion = models.DateTimeField()

    def __str__(self):
        return self.nom_user.capitalize()

    class Meta:
        db_table = 'user'