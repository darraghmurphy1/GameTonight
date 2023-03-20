from django import forms
from .models import Favourite


class FavouriteForm(forms.ModelForm):

    class Meta:
        model = Favourite
        fields = ('post',)
 