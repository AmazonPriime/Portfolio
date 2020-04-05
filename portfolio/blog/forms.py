from django import forms
from ckeditor.widgets import CKEditorWidget
from blog.models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Title', 'id' : 'id_title'}))
    content = forms.CharField(widget = CKEditorWidget())

    class Meta:
        model = Post
        fields = ('title', 'content',)