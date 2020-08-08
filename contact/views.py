from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            apellido = request.POST.get('apellido', '')
            celular = request.POST.get('celular', '')
            email = request.POST.get('email', '')
            asunto = request.POST.get('asunto', '')
            content = request.POST.get('content', '')

            # Creamos el correo
            email = EmailMessage(
                "Keratech: Nuevo mensaje de contacto",
                "De {}{} <{}> <{}>\n\nAsunto:\n\n{}\n\nEscribió:\n\n{}".format(name, apellido, email, celular, asunto, content),
                "no-contestar@keratech.pe",
                ["keratechperu@gmail.com"],
                reply_to=[email]
            )

            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok#seccion-contacto")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail#seccion-contacto")
    
    return render(request, "contact/contact.html",{'form':contact_form})

    