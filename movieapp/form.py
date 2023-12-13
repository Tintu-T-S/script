from django import forms
from .models import cinema_table

class cinemaform(forms.ModelForm):
    class Meta:
        model=cinema_table
        fields=['name','desc','year','img']