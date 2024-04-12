from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ('author', 'post', 'date_created', 'date_modified')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('author', 'date_modified', 'date_created')


class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('caption',)