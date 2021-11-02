from django import forms
from django.db.models import fields
from .models import Vehiculo


class formularioVehiculo(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'