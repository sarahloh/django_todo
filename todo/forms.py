from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    # inner class provides extra info to django about the form
    class Meta:
        model = Item
        fields = ('name', 'done')