from django import forms
from .models import vehicle, centre, elder

class VehicleForm(forms.ModelForm):
    class Meta:
        model = vehicle
        fields = '__all__'

class CentreForm(forms.ModelForm):
    class Meta:
        model = centre
        fields = '__all__'

class ElderForm(forms.ModelForm):
    class Meta:
        model = elder
        fields = '__all__'
