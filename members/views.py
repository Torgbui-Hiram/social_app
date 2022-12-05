from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, "Login Success")
            return redirect('home')
        else:
            messages.success(
                request, 'Sorry There Was An Error Loging Inn, Please try again....')
            return redirect('')

    else:
        return render(request, 'authentication/login.html', {})


# Logout user
def logout_user(request):
    logout(request)
    messages.success(
        request, 'You were Logged out!!!')
    return redirect('home')


# New user signup
def sign_up(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            # save form in the memory not in database
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('authentication/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            receiver_email = form.cleaned_data.get("email")
            sender_mail = EMAIL_HOST_USER
            send_mail(
                mail_subject, message, sender_mail, recipient_list=[receiver_email, ], fail_silently=False)
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = RegisterUserForm()
    return render(request, 'authentication/register_user.html', {'form': form})


# Activating account
def activate(request, uidb64, token):

    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        user.backend = "django.contrib.auth.backends.ModelBackend"
        messages.success(
            request, f'Hi {user} thank you for your email confirmation. Please login to continue!')
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')
