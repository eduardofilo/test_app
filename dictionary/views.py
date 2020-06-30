from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from dictionary.forms import AcceptationFormSet, WordForm
from dictionary.models import Word


class WordListView(generic.ListView):
    model = Word


class WordCreateView(generic.CreateView):
    model = Word
    success_url = reverse_lazy('dictionary:word_list')
    form_class = WordForm

    def get_context_data(self, **kwargs):
        data = super(WordCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['acceptations'] = AcceptationFormSet(self.request.POST)
        else:
            data['acceptations'] = AcceptationFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        acceptations = context['acceptations']
        with transaction.atomic():
            self.object = form.save()
            if acceptations.is_valid():
                acceptations.instance = self.object
                acceptations.save()
        return super(WordCreateView, self).form_valid(form)


class WordUpdateView(generic.UpdateView):
    model = Word
    success_url = reverse_lazy('dictionary:word_list')
    form_class = WordForm

    def get_context_data(self, **kwargs):
        data = super(WordUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['acceptations'] = AcceptationFormSet(self.request.POST, instance=self.object)
        else:
            data['acceptations'] = AcceptationFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        acceptations = context['acceptations']
        with transaction.atomic():
            self.object = form.save()
            if acceptations.is_valid():
                acceptations.instance = self.object
                acceptations.save()
        return super(WordUpdateView, self).form_valid(form)


class WordDeleteView(generic.DeleteView):
    model = Word
    success_url = reverse_lazy('dictionary:word_list')
