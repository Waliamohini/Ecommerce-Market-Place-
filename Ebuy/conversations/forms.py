from django import forms
from .models import ConvMessages



class ConversationMessage(forms.ModelForm):
    class Meta:
        model = ConvMessages
        fields = ('content',)
        widgets = {
            'content' : forms.Textarea(attrs = {
                'class' : 'p-5 rounded-xl w-full border'
            } )
        }