from django.shortcuts import render
from .models import Etudiant
from .models import Timedepointage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def afficher_etudiant(request, id):
    if request.method == 'GET':
        etudiant = Etudiant.objects.filter(id=id).first()
        if etudiant:
            return JsonResponse({
                'id':etudiant.id,
                #'prenom':etudiant.prenom,
                'nom':etudiant.nom,
                'email':etudiant.email,
                'code_barre':etudiant.code_barre
            }, status=200)
        else:
            return JsonResponse({'message':'etudiant Indisponible'})

    if request.method == 'POST':
        return JsonResponse({'message':'methode post non prise en charge'}, status=404)
def afficher_etudiants(request):
    if request.method =='GET':
        data_etudiants = []
        etudiants=Etudiant.objects.all()
        for etudiant in etudiants:
            data={
                'id':etudiant.id,
                #'prenom':etudiant.prenom,
                'nom':etudiant.nom,
                'email':etudiant.email,
                'code_barre':etudiant.code_barre
            }
            data_etudiants.append(data)
        return JsonResponse(data_etudiants, status=200, safe=False)
        
    if request.method == 'POST':
        return JsonResponse({'message':'methode post non prise en charge'}, status=404)

@csrf_exempt
def create_etudiant(request):
    if request.method =='POST':
        #vprenom=request.POST.get('prenom')
        vnom=request.POST.get('nom')
        vemail=request.POST.get('email')
        vcode_barre=request.POST.get('code_barre')
        vphoto=request.POST.get('photo')
        vnumero_de_telephone=request.POST.get('numero_de_telephone')
        etudiant=Etudiant.objects.create(nom=vnom,email=vemail,photo=vphoto,code_barre=vcode_barre,numero_de_telephone=vnumero_de_telephone)
        if etudiant:
                return JsonResponse({
                    'photo': etudiant.photo.url if etudiant.photo else None,
                    'id':etudiant.id,
                    'nom':etudiant.nom,
                    'email':etudiant.email,
                    'code_barre':etudiant.code_barre
                }, status=200)
        

"""def afficher_detail(request,code_barre):

    etudiant=Etudiant.objects.get(code_barre=code_barre)
    if etudiant:
        data={
            'id':etudiant.id,
          #  'prenom':etudiant.prenom,
            'nom':etudiant.nom,
            'email':etudiant.email,
            'code_barre':etudiant.code_barre,
            'photo': etudiant.photo
        }

        return JsonResponse(data,status=200)"""

@csrf_exempt
def afficher_detail(request):
    if request.method == 'POST':
        code_barre = request.POST.get('code_barre')
        etudiant = Etudiant.objects.filter(code_barre=code_barre).first()
        
        if etudiant:
            data = {
                'id': etudiant.id,
                'nom': etudiant.nom,
                'email': etudiant.email,
                'code_barre': etudiant.code_barre,
                'photo': etudiant.photo.url if etudiant.photo else None 
            }
            return JsonResponse(data, status=200)
        else:
            return JsonResponse({'error': 'Étudiant non trouvé'}, status=404)
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
def update_etudiant(request,pk):
   
    if request.method =='POST':
        vnom= request.POST.get('nom')
        #vprenom=request.POST.get('prenom')
        vemail=request.POST.get('email')
        vcode_barre=request.POST.get('code_barre')
        etudiant=Etudiant.objects.get(id=pk)
        
    if etudiant:
        if vnom:
            etudiant.nom=vnom
        if vnumero_de_telephone:
            etudiant.numero_de_telephone=vnumero_de_telephone
        if vemail:
            etudiant.email=vemail
        data={
            'nom':etudiant.nom,
            #'prenom':etudiant.prenonm,
            'email':etudiant.email,
            'photo':etudiant.photo,               
            'code_barre':etudiant.code_barre
        }
        etudiant.save()
     
        return JsonResponse(data,status=200)
    else:
        return JsonResponse({'message':'etudiant non trouvé '},status=404)

"""
@csrf_exempt
def enregistrer_log(request):
    if request.method == 'POST':
        code_barre=request.POST.get('code_barre')
        etudiant=Etudiant.objects.get(code_barre=code_barre)
        if etudiant:
            
            log=Timedepointage.objects.create(id_etudiant=etudiant)
            data={
                'idlog':log.id_etudiant.id,
                'timelog':log.time,
                 'nom':log.id_etudiant.nom,
                 'email':log.id_etudiant.email,
                 'photo':log.id_etudiantphoto.url
            }
            return JsonResponse(data,status=200)
        else:
            return JsonResponse({'error'
            :'code barre not found'}, status=404)
"""
@csrf_exempt
def enregistrer_log(request):
    if request.method == 'POST':
        code_barre = request.POST.get('code_barre')
        try:
            etudiant = Etudiant.objects.get(code_barre=code_barre)
            log = Timedepointage.objects.create(id_etudiant=etudiant)
            data = {
                'idlog': log.id,  # Utilisez log.id pour l'identifiant du log
                'timelog': log.time,
                'nom': log.id_etudiant.nom,
                'email': log.id_etudiant.email,
                'photo': log.id_etudiant.photo.url if log.id_etudiant.photo else None
            }
            return JsonResponse(data, status=200)
        except Etudiant.DoesNotExist:
            return JsonResponse({'error': 'code barre not found'}, status=404)
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)