from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class Registroform(UserCreationForm):
        username = forms.CharField(label="Usuario", 
        widget= forms.TextInput(attrs={'class':'input-registro','placeholder':'Nombre de Usuario'}))

        password1 = forms.CharField(label="Contraseña",
        widget= forms.PasswordInput(attrs={'class':'input-registro','placeholder':'contraseña'}))
        
        password2 = forms.CharField(label="Repetir Contraseña",
        widget= forms.PasswordInput(attrs={'class':'input-registro', 'placeholder':'confirmar contraseña'}))

        email = forms.CharField(label="Email",
        widget= forms.EmailInput(attrs={'name': 'email-registro','placeholder':'Correo Electronico','class': 'input-registro','required':True}))
        nombre = forms.CharField(label="Nombre", max_length=20, min_length=3,
        widget= forms.TextInput(attrs={'type': 'text','placeholder':'Nombre','class': 'input-registro','required':True}))  

        apellido = forms.CharField(label="Apellido",max_length=25,min_length=3,
        widget= forms.TextInput(attrs={'type': 'text','placeholder':'Apellido', 'class': 'input-registro', 'required':True }))

        dni= forms.CharField(label="DNI",max_length=8,min_length=8,
        widget= forms.TextInput(attrs={'type': 'text','placeholder':'DNI','class': 'input-registro','class': 'input-registro','required':True }))  

        direccion= forms.CharField(label="Dirección",
        widget= forms.TextInput(attrs={'type': 'text', 'placeholder':'Dirección', 'class': 'input-registro','required':True}))

        def __init__(self, *args, **kwargs):
                super(Registroform, self).__init__(*args, **kwargs)

                for fieldname in ['username', 'password1', 'password2']:
                        self.fields[fieldname].help_text = None

        class Meta:
                model = User
                fields =  ['username', 'password1', 'password2','email','nombre','apellido','dni','direccion']



class ContactoMensaje(forms.Form):

        Nombre = forms.CharField(max_length=20, min_length=3,label='Nombre',
        widget= forms.TextInput(attrs={'type': 'text','placeholder':'Su nombre','class': 'input-contacto','required':True}))

        email_contacto = forms.CharField(label="Email",
        widget= forms.EmailInput(attrs={'name': 'email-contacto','placeholder':'Su Email','class': 'input-contacto','required':True}))

        Asunto = forms.CharField(max_length=20, min_length=3,label='Asunto',
        widget= forms.TextInput(attrs={'type': 'text','placeholder':'Asunto','class': 'input-asunto','required':True}))

        Comentario = forms.CharField(max_length=300, min_length=10,label='Comentario',
        widget= forms.TextInput(attrs={'type': 'textarea','placeholder':'Mensaje','class': 'input-comentario','required':True}))



