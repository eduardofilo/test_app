from django import forms
from .models import *
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .layouts import *
from django.utils.translation import gettext as _


class AcceptationForm(forms.ModelForm):
    class Meta:
        model = Acceptation
        exclude = ()
        widgets = {
            'meaning': forms.Textarea(attrs={'rows': 2, 'cols': 70}),
        }

    def __init__(self, *args, **kwargs):
        super(AcceptationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


AcceptationFormSet = inlineformset_factory(
    Word, Acceptation, form=AcceptationForm, fields=['meaning'], extra=1, can_delete=True)


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        exclude = []

    def __init__(self, *args, **kwargs):
        super(WordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_show_labels = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('term'),
                Fieldset('Acepciones',
                    Formset('acceptations')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'Guardar')),
                )
            )


class FilterForm(forms.Form):
    filter = forms.CharField(max_length=100, required=False)

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.fields['filter'].widget.attrs['placeholder'] = _('Filtrar')
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
