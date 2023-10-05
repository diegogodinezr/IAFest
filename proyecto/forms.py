from multiprocessing.sharedctypes import Value
from django import forms
from .models import *
from django.utils import timezone

class TablaForm(forms.ModelForm):
    class Meta:
        model = Tabla
        fields = '__all__'