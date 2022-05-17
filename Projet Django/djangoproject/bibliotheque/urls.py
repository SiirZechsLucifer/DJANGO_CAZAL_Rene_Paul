from django.urls import path

from . import views

urlpatterns = (
    #Manga
    path('index/', views.index),
    path('ajout/<int:id>/', views.ajout),
    path('traitement/<int:id>/', views.traitement),
    path('affiche/<int:id>/', views.affiche),
    path('home/', views.home),
    path('delete/<int:id>/', views.delete),
    path('traitementupdate/<int:id>/', views.traitementupdate),
    path('update/<int:id>/', views.update),
    path('manga/<int:id>', views.manga),
    #Genre
    path('ajoutgenre/', views.ajoutgenre),
    path('updategenre/<int:id>/', views.updategenre),
    path('traitementupdategenre/', views.traitementupdate),
    path('deletegenre/<int:id>/', views.deletegenre),
    path('affichegenre/<int:id>/', views.affichegenre),
    path('traitementgenre/', views.traitementgenre),


)
