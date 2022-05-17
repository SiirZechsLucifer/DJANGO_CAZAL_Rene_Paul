from django.db import models


# Create your models here.
class Manga(models.Model):

    titre = models.CharField(max_length=100)  # défini un champs de type texte de 100caractères maximum

    auteur = models.CharField(max_length=100)

    date_parution = models.DateField(blank=True,
                                     null=True)  # champs de type date,pouvant être null ou ne pas être rempli

    nombre_pages = models.IntegerField(blank=False)  # champs de type entier devantêtre obligatoirement rempli

    resume = models.TextField(null=True, blank=True)  # champs de type text long

    def __str__(self):
        chaine = f"{self.titre}␣écrit par {self.auteur} édité le {self.date_parution}"

        return chaine

    def __str__(self):
        chain = f"{self.titre} {self.auteur} {self.date_parution} {self.nombre_pages} {self.resume}"
        return chain


    def dico(self):
        return {"titre": self.titre, "auteur": self.auteur, "date de parution": self.date_parution,
                "nombre de pages": self.nombre_pages, "résumé": self.resume}


class Genre(models.Model):
    nom = models.CharField(max_length=100)  # défini un champs de type texte de 100caractères maximum

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine

    def dico(self):
        return {"Genre": self.nom}
