from django import forms
from contacts_app.models import Contact

class AddContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ('manager',)


class UpdateContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ('manager',)