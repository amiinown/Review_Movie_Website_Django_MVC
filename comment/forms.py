from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'نظر خود را بنویسید...',
                'rows': 3,
            })
        }
        labels = {
            'content':'',
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'نظر خود را بنویسید...',
                'rows': 1,
            })
        }
        labels = {
            'content':'',
        }