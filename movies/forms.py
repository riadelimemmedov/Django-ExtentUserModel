from django import forms
from actors.models import *
from .models import *

MOVIE_CHOICES = (
    ('FILM','Film'),
    ('COMMERCIAL','Commercial')
)

class MovieSelectForm(forms.Form):
    movie_select = forms.ChoiceField(choices=MOVIE_CHOICES, label='',widget=forms.RadioSelect(attrs={'class':'radio_1'}))
    
class FilmModelForm(forms.ModelForm):
    actors = forms.ModelMultipleChoiceField(label='Select all the actors',widget=forms.SelectMultiple,queryset=Actor.objects.filter(is_star=True))
    class Meta:
        model = Film
        fields = '__all__'
        
class CommercialForm(forms.ModelForm):
    actors = forms.ModelMultipleChoiceField(label='Select all the actors',widget=forms.SelectMultiple,queryset=Actor.objects.filter(is_star=False))
    class Meta:
        model = Commercial
        fields = '__all__'