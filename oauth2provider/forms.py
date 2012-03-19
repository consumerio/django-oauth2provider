from django import forms

class CreateClientForm(forms.Form):
    
    name = forms.CharField(label="Name", max_length=30)


class RemoveClientForm(forms.Form):

    client_id = forms.IntegerField()