from django import forms

from .models import Filters

class PrefForm(forms.ModelForm):

    class Meta:
        model = Filters
        fields = ('category',)
#        exclude = ('user',)

