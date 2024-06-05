from django.urls import path
from . import views

urlpatterns = [
    path('etudiants/<int:code_barre>', views.afficher_etudiant_code, name='details-etudiant-code'),
    path('etudiants/', views.all_etudiant, name='all-etudiant'),
]