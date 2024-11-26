from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'is_favorite']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        
       
        if not name:
            raise forms.ValidationError("Имя не может быть пустым.")
        
      
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError("Имя должно содержать только буквы и пробелы.")
        
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        
        return phone
