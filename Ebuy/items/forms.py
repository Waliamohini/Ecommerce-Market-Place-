from django import forms
from .models import Item

input_class = 'px-3 py-5 border rounded-xl m-4 mx-4 w-full'
class NewItemForm(forms.ModelForm):
    class Meta : 
        model = Item
        
        fields = ('Name', 'Description', 'Image', 'Price', 'Category')
        
        widgets = { 
                  'Category' : forms.Select(attrs = {
                      'class' : input_class
                  }),
                  
                  'Name' : forms.TextInput(attrs = {
                      'class' : input_class
                  }),
                  'Description' : forms.Textarea(attrs = {
                      'class' : input_class
                  }),
                  'Price' : forms.TextInput(attrs = {
                      'class' : input_class
                  }),
                  'Image' : forms.FileInput(attrs = {
                      'class' : input_class
                  })
                  }
        
class EditItemForm(forms.ModelForm):
    class Meta : 
        model = Item
        
        fields = ('Name', 'Description', 'Image', 'Price')
        
        widgets = { 
                  
                  'Name' : forms.TextInput(attrs = {
                      'class' : input_class
                  }),
                  'Description' : forms.Textarea(attrs = {
                      'class' : input_class
                  }),
                  'Price' : forms.TextInput(attrs = {
                      'class' : input_class
                  }),
                  'Image' : forms.FileInput(attrs = {
                      'class' : input_class
                  })
                  }