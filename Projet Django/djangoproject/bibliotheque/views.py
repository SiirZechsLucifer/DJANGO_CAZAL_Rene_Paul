from django.shortcuts import render
from .forms import MangaForm
from .forms import GenreForm

from . import models
from django.http import HttpResponseRedirect


# Create your views here.

def index(request):
    return render(request, 'bibliotheque/index.html')


def ajout(request, id):
    form = MangaForm()  # création d'un formulaire vide
    return render(request, "bibliotheque/ajout.html", {"form": form, "id": id})


def traitement(request, id):
    genre = models.Genre.objects.get(pk=id)
    mform = MangaForm(request.POST)
    if mform.is_valid():
        manga = mform.save(comit=False)
        manga.genre = genre
        manga.genre_id = id
        manga.save()
        return HttpResponseRedirect("/bibliotheque/manga/")
    else:
        return render(request, "bibliotheque/ajout.html", {"form": mform})


def affiche(request, id):
    manga = models.Manga.objects.get(pk=id)  # méthode pour récupérer les données dans la base avec un id donnée
    return render(request, "bibliotheque/affiche.html", {"manga": manga})


def traitementupdate(request, id):
    mform = MangaForm(request.POST)
    if mform.is_valid():
        manga = mform.save(
            commit=False)  # création d'un objet livre avec les données duformulaire mais sans l'enregistrer dans la base.

        manga.id = id;  # modification de l'id de l'objet
        manga.save()  # mise à jour dans la base puisque l'id du livre existe déja.
        return HttpResponseRedirect(
            "/bibliotheque/")  # plutot que d'avoir un gabaritpour nous indiquer que cela c'est bien passé, nous repartons sur une autre actionqui renvoie vers la page d'index de notre site (celle avec la liste des entrées)
    else:
        return render(request, "bibliotheque/update.html", {"form": mform, "id": id})


def delete(request, id):
    manga.delete()
    return HttpResponseRedirect("/bibliotheque/manga")


#def home(request):
    #liste = list(models.Manga.objects.all())

    #return render(request, 'bibliotheque/home.html', {"liste": liste})


def update(request, id):
    manga = models.Manga.objects.get(pk=id)
    mform = MangaForm(manga.dico)
    return render(request, "bibliotheque/update.html", {"form": mform, "id": id})


def manga(request):
    liste = list(models.Manga.objects.all())

    return render(request, 'bibliotheque/manga.html', {"liste": liste})


def ajoutgenre(request):
    form = GenreForm()  # création d'un formulaire vide
    return render(request, "bibliotheque/ajoutgenre.html", {"form": form})



def traitementgenre(request):

    gform = GenreForm(request.POST)
    if gform.is_valid():
        genre = gform.save()
        return HttpResponseRedirect('/bibliotheque/home')
    else:
        return render(request, "bibliotheque/ajoutgenre.html", {"form": gform})


def affichegenre(request, id):
    genre = models.Genre.objects.get(pk=id)  # méthode pour récupérer les données dans la base avec un id donnée

    return render(request, "bibliotheque/affichegenre.html", {"genre": genre})


def traitementupdategenre(request, id):
    genre = models.Genre.objects.get(pk=id)
    gform = GenreForm(request.POST)
    if gform.is_valid():
        genre = gform.save(
            commit=False)  # création d'un objet livre avec les données duformulaire mais sans l'enregistrer dans la base.

        genre.id = id;  # modification de l'id de l'objet
        genre.save()  # mise à jour dans la base puisque l'id du livre existe déja.
        return HttpResponseRedirect(
            "/bibliotheque/")  # plutot que d'avoir un gabaritpour nous indiquer que cela c'est bien passé, nous repartons sur une autre actionqui renvoie vers la page d'index de notre site (celle avec la liste des entrées)
    else:
        return render(request, "bibliotheque/updategenre.html", {"form": gform, "id": id})


def deletegenre(request, id):
    genre = models.Genre.objects.get(pk=id)
    genre.delete()
    return HttpResponseRedirect("/bibliotheque/home")


def home(request):
    liste = list(models.Genre.objects.all())

    return render(request, 'bibliotheque/home.html', {"liste": liste})


def updategenre(request, id):
    genre = models.Genre.objects.get(pk=id)
    gform = GenreForm(genre.dico)
    return render(request, "bibliotheque/updategenre.html", {"form": gform, "id": id})
