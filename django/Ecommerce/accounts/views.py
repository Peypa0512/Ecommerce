from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
# importamos las clases para el envio del correo
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage


# Create your views here.
def register(request):
    #vamos a capturar la data que envia el cliente...
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid(): # si ha pasado la validacion
            # capturamos los datos
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # para el user name vamos a capturar el email y sobre él lo vamos a hacer
            username = email.split('@')[0]

            # instancia al usuario
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                               username=username, password=password)
            user.phone_number = phone_number
            user.save()

            # creamos el proceso de envio de correo
            current_site = get_current_site(request)
            mail_subject = 'Por favor activa tu cuenta....'
            body = render_to_string('accounts/account_verification_email.html', {
                'user': user,  # el nombre y datos del usuario
                'domain': current_site,  # le vamos a pasar nuestro dominio
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),  # va a codificar como  adas34523d
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_mail = EmailMessage(mail_subject, body, to=[to_email])
            send_mail.send()

            #messages.success(request, 'Se ha registrado correctamente')
            return redirect('/accounts/login/?command=Verification&email='+email)


    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # ahora autentificamos...
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario y Contraseña no correcto')
            return redirect('login')



    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Has cerrado sesión')

    return redirect('login')


def activate(request, uidb64, token):   # esto se hará cuando el usuario le de al click de activar la cuenta
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Tu cuenta ya está activa')
        return redirect('login')
    else:
        messages.error(request, 'La activación ha dado algún tipo de error')
        return redirect('register')
