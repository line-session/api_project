from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home', views.home, name='home'),
    path('etudiant/afficher/<int:id>', views.afficher_etudiant, name='details-etudiant'),
    path('etudiant/afficher-etudiants', views.afficher_etudiants ,name='etudiants'),
    path('etudiant/create-etudiant', views.create_etudiant, name='creer-etudiant'),
    path('etudiant/afficher-etudiant/' ,views.afficher_detail,name='afficher-etudiant'),
    path('etudiant/update-etudiant' ,views.update_etudiant,name='update-etudiant'),
    path('etudiant/enregistrer-log/',views.enregistrer_log ,name='enregistrer-log')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)