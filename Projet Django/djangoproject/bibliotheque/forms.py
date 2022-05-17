from django.forms import ModelForm

from django.utils.translation import gettext_lazy as _

from . import models


class MangaForm(ModelForm):
    class Meta:
        model = models.Manga
        fields = ('titre', 'auteur', 'date_parution', 'nombre_pages', 'resume')
        labels = {
            'titre': _('Titre'),
            'auteur': _('Auteur'),
            'date_parution': _('date de parution'),
            'nombre_pages': _('nombres de pages'),
            'resume': _('Résumé')
        }


class GenreForm(ModelForm):
    class Meta:
        model = models.Genre
        fields = ('nom',)
        labels = {
            'nom': _('Nom',)

        }
