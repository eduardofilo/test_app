from django.conf import settings
from django.db import transaction
from django.urls import reverse_lazy
from django.views import generic

from dictionary.forms import AcceptationFormSet, WordForm, FilterForm
from dictionary.models import Word


class WordListView(generic.ListView):
    model = Word
    paginate_by = settings.PAG_WORD

    def get_queryset(self):
        filter = self.request.GET.get('filter', "")
        if filter == "":
            words = super(WordListView, self).get_queryset()
        else:
            words = Word.objects.filter(term__icontains=filter).order_by('term')

        return words

    def get_context_data(self, **kwargs):
        context = super(WordListView, self).get_context_data(**kwargs)

        filter = self.request.GET.get('filter')
        if filter == "":
            context['form'] = FilterForm()
        else:
            context['form'] = FilterForm(initial={'filter': filter})

        return context


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


class WordDeleteView(generic.base.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        word = Word.objects.get(pk=self.kwargs['pk'])
        if word:
            word.delete()

        self.url = reverse_lazy('dictionary:word_list')
        return super(WordDeleteView, self).get_redirect_url(*args, **kwargs)