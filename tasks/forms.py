from django import forms
from .models import Task

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'is_completed')

        widgets= {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'})
        }