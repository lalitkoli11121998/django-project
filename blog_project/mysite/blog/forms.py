from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):


    class Meta():
        model = Post
        fields = ('author', 'title', 'text')
        # medium-editor-textarea this class apply the plugin the textarea field 
        # user can change color, font, spell of the text 
        widgets = {
            'title' : forms.TextInput(attrs={'class':'textinputclass'}),
            'text' : forms.Textarea(attrs ={'class': 'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')
        
        # textinputclass is a custom css class which we are using for styling
        widgets = {
            'author' : forms.TextInput(attrs={'class':'textinputclass'}),
            'text' : forms.Textarea(attrs ={'class': 'editable medium-editor-textarea'})
        }