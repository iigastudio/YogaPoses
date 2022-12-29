# Import ModelForm
from django import forms
from .models import Yoga

# Create yoga form
class YogaForm(forms.ModelForm):
    class Meta:
        model = Yoga
        fields = '__all__'
        exclude = ['posted_by', 'updated_at', 'created_at']
        enctype = "multipart/form-data"
        