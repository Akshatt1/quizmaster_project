from django import forms
from .models import quiz

class quizForm(forms.ModelForm):
    class Meta:
        model = quiz
        fields = ('title', 'photo', 'data')

        



        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter quiz title'}),
            'data': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter quiz data'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file','accept': 'photo/*' })
        }
