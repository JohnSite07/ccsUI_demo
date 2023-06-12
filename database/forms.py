from django import forms
from .variables import *

class DataQueryForm(forms.Form):
    tableau = forms.ChoiceField(choices=list_tuple(list_vues))