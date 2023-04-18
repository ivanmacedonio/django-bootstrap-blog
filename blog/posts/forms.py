from django.forms import ModelForm
from django import forms 
from .models import *

class PostForm(ModelForm): #Modelform hace que se cree automaticamente la interfaz de formulario en el HTML 
    class Meta:
        model = Post
        fields = '__all__'

