from django import forms
from django.contrib.auth.models import User


class CursoFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    comision = forms.IntegerField(required=True, max_value=50000)



