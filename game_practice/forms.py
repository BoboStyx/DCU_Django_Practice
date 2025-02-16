from django import forms
from .models import *



class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['Name','Description','Price','Number_In_Stock','Game_Platform','Game_Genre']
    
    def clean(self):
        data = self.cleaned_data
        Game_Genre = data['Game_Genre']

        if Game_Genre != Game_Genre.lower():
            raise forms.ValidationError("Genre must be in lower case")
        
        return data