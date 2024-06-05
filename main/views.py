from django.shortcuts import render
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# cette methode permet d'afficher un etudiant par son code barre
def afficher_etudiant_code(request, code_barre):
    if request.method == 'GET':
        etudiant = User.objects.filter(code_bar=code_barre).first()
        if etudiant:
            return JsonResponse({
                'user':etudiant.nom_user,
                'email':etudiant.email,
                'code_barre':etudiant.code_bar,
                'photo':etudiant.photo,
                'heure_connexion':etudiant.heure_connexion,
                'number_user':etudiant.number_user
            }, status=200)
        else:
            return JsonResponse({'message':'etudiant indisponible'})

    if request.method == 'POST':
        return JsonResponse({'message':'methode post non prise en charge'}, status=404)
    
# cette methode permet d'afficher tous les etudiants
def all_etudiant(request):
    if request.method == 'GET':
        etudiants = User.objects.all()
        data = []
        for etudiant in etudiants:
            data.append({
                'user':etudiant.nom_user,
                'email':etudiant.email,
                'code_barre':etudiant.code_bar,
                'photo':etudiant.photo,
                'heure_connexion':etudiant.heure_connexion,
                'number_user':etudiant.number_user
            })
        return JsonResponse(data, status=200, safe=False)

    if request.method == 'POST':
        return JsonResponse({'message':'methode post non prise en charge'}, status=404)
        

       