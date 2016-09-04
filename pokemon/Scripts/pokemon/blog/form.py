from django import forms
from .models import Monster,Type

class PostForm(forms.ModelForm):
    class Meta:
        model = Monster
        fields = ('pokemon_id','name','type','content')