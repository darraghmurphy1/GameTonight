from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        body = forms.CharField(widget=forms.Textarea, label='')
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """ Form for post submission """
    class Meta:
        model = Post
        fields = ('title', 'content')
