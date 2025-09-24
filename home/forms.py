from django import forms
from .models import Comment,Message

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your comment'}),
        }



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'phone', 'message']  # include phone
