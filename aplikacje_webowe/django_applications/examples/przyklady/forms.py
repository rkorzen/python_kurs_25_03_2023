from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Imię', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    message = forms.CharField(label='Wiadomość', max_length=1000, widget=forms.Textarea)
    isue_date = forms.DateTimeField(label='Data zgłoszenia', required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.capitalize()
