from django.shortcuts import render
from .models import Etudiant
from .models import Timedepointage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@csrf_exempt
def enregistrer_log(request):
    if request.method == 'POST':
        code_barre = request.POST.get('code_barre')
        try:
            etudiant = Etudiant.objects.filter(code_bar=code_barre).first()
            log = Timedepointage.objects.create(id_etudiant=etudiant)
            data = {
                'idlog': log.id,  # Utilisez log.id pour l'identifiant du log
                'timelog': log.time,
                'nom': log.id_etudiant.nom_user,
                'email': log.id_etudiant.email,
                'photo': log.id_etudiant.photo.url if log.id_etudiant.photo else None
            }
            return JsonResponse(data, status=200)
        except Etudiant.DoesNotExist:
            return JsonResponse({'error': 'code barre not found'}, status=404)
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)