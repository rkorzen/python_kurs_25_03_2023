from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from django import forms
from django.forms import formset_factory

from .models import Book

CATEGORY_CHOICES = (
    ('fantasy', 'Fantastyka'),
    ('horror', 'Horror'),
    ('sci-fi', 'Science Fiction'),
    ('romance', 'Romans'),
    ('thriller', 'Thriller'),
)

class BookForm(forms.Form):
    title = forms.CharField(label='Tytuł', max_length=256)
    author = forms.CharField(label='Autor', max_length=256)
    description = forms.CharField(label='Opis', max_length=1000, widget=forms.Textarea)
    cover_image = forms.ImageField(label='Okładka', required=False)
    category = forms.ChoiceField(label='Kategoria', required=False, choices=CATEGORY_CHOICES)

    def clean_title(self):
        title = self.cleaned_data['title']
        return title.capitalize()

    def clean_author(self):
        author = self.cleaned_data['author']
        return author.title()

class BookForm2(forms.ModelForm):
    category = forms.ChoiceField(label='Kategoria', required=False, choices=CATEGORY_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset("Dodawanie Posta", "title", "author", "description", "cover_image", "category"),
            Submit("submit", "Zapisz"),
        )
    class Meta:
        model = Book
        fields = "__all__"


    def clean_title(self):
        title = self.cleaned_data['title']
        return title.capitalize()

    def clean_author(self):
        author = self.cleaned_data['author']
        return author.title()


class MyForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')

MyFormSet = formset_factory(MyForm, extra=2)