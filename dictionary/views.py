from django.shortcuts import render
from django.views import generic


class WordListView(generic.TemplateView):
    template_name = 'dictionary/home.html'