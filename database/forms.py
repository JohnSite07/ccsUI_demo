from django import forms

class DataQueryForm(forms.Form):
    tableau = forms.CharField(max_length=100)