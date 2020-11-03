from django import forms
from django.forms import ModelForm
from .models import contactform


class rooba(forms.ModelForm):
     
    class Meta:
        FRUIT_CHOICES= [
        ('select any one', 'select any one'),   
        ('orange', 'Oranges'),
        ('cantaloupe', 'Cantaloupes'),
        ('mango', 'Mangoes'),
        ('honeydew', 'Honeydews'),
        ]
        model = contactform
        fields = ['name', 'email', 'phone' ,'subject', 'message']

        widgets ={
            'name' : forms.TextInput(attrs ={'class':'form-control','type':'input', 'placeholder':'Your name','name':'name'}),
            'email' : forms.TextInput(attrs ={'class':'form-control', 'placeholder':'Your Email','name':'email'}),
            'phone' : forms.TextInput(attrs ={'class':'form-control', 'placeholder':'Phone no.','name':'phone'}),
            'subject' : forms.Select(attrs ={'class':'form-control', 'placeholder':'Select Subject','name':'subject'}, choices=FRUIT_CHOICES ),
            'message' : forms.Textarea(attrs ={'class':'form-control', 'placeholder':'Message','name':'message'}),
        }
