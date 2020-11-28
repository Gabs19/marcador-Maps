from django import forms
from .models import PointerMarker


class PointerMarkerModelForm(forms.ModelForm):
    class Meta:
        model = PointerMarker
        fields = ('nome_local','latitude','longitude')