from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from dictionary.models import Word


class WordListView(generic.ListView):
    model = Word

class WordCreateView(generic.CreateView):
    model = Word
    fields = ['term']
    success_url = reverse_lazy('dictionary:word_list')

class WordDetailView(generic.UpdateView):
    model = Word
    fields = ['term']
    success_url = reverse_lazy('dictionary:word_list')

class WordDeleteView(generic.DeleteView):
    model = Word
    success_url = reverse_lazy('dictionary:word_list')
