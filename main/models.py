from django.db import models

# Create your models here.
class Etudiant(models.Model):
    nom_user = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    number_user = models.IntegerField(blank=True, null=True)
    photo = models.FileField(upload_to='photos/')
    code_bar = models.CharField(max_length=255, blank=True, null=True)
    heure_connexion = models.DateTimeField()

    def __str__(self):
        return self.nom_user.capitalize()

    class Meta:
        db_table = 'user'

class Timedepointage(models.Model):
    id= models.AutoField(primary_key=True)
    time= models.DateTimeField(auto_now_add=True)
    id_etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_etudiant} - {self.time}"
    