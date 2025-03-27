from django import forms
from .models import Post, Comments, Profile

class PostForm(forms.ModelForm):
    body = forms.CharField(label= '', widget=forms.Textarea(attrs={
        'row':'3',
        'placeholder':'Say Something....'
    }))
    class Meta:
        model = Post
        fields = ['body']

class CommentForm(forms.ModelForm):
    comments = forms.CharField(label= '', widget=forms.Textarea(attrs={
        'row':'3',
        'placeholder':'Say Something....'
    }))
    class Meta:
        model = Comments
        fields = ['comments']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'bio', 'birth_date', 'location', 'picture']
    