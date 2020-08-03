from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control pl-5', 'placeholder':'Tu nombre'}
    ), min_length=3, max_length=100)
    apellido = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(
        attrs={'class':'form-control pl-5', 'placeholder':'Tu apellido'}
    ), min_length=3, max_length=100)
    celular = forms.CharField(label="Celular", required=True, widget=forms.TextInput(
        attrs={'class':'form-control pl-5', 'placeholder':'Numero de contacto'}
    ), min_length=7, max_length=12)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control pl-5', 'placeholder':'Escribe tu email'}
    ), min_length=3, max_length=100)
    asunto = forms.CharField(label="Asunto", required=True, widget=forms.TextInput(
        attrs={'class':'form-control pl-5', 'placeholder':'Asunto'}
    ), min_length=3, max_length=200)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control pl-5', 'rows': 4, 'placeholder':'Escribe tu mensaje...'}
    ), min_length=10, max_length=1000)
    