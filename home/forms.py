from django import forms

class MovieActorSearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control me-2', 'placeholder':'فیلم یا بازیگر"'}))