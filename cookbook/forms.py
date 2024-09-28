from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    form_id = forms.CharField(widget=forms.HiddenInput(), initial='comment_form')
    
    class Meta:
        model = Comment
        fields = ('comment_selection','own_comment',)
    
    
        