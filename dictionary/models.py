from django.db import models
from django.utils.translation import ugettext as _


# Word model
class Word(models.Model):
    term = models.CharField(_('palabra'), max_length=100, blank=False, null=False)


# Acceptation model
class Acceptation(models.Model):
    meaning = models.TextField(_('acepción'), max_length=4096, blank=False)
    word = models.ForeignKey('Word', on_delete=models.CASCADE, blank=False, null=False)