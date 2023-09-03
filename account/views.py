from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from .forms import ContactForm, UserCreateForm
from user_profile.models import UserProfile
from django.db.models import Q


# def home(request):
#     return render(request, 'account/home.html')

def aboutus(request):
    return render(request, 'account/aboutus.html')
def thankyou(request):
    return render(request, 'account/thankyou.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:thankyou') 
    else:
        form = ContactForm()
    
    return render(request, 'account/contact.html', {'form': form})


def SignUp(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = user.first_name
            last_name = user.last_name
            name = first_name + ' ' + last_name
            UserProfile.objects.create(name=name, user=user)
            login(request, user)
            return redirect('account:home')
    else:
        form = UserCreateForm()
    return render(request, 'account/signup.html', {'form': form})


# @login_required(login_url='/login/')
def home(request):
    if request.method == "GET":
        context = {
            "pat_list": UserProfile.objects.filter(Q(user__user_type="P") | Q(user__user_type="D"))[:5]
        }
        return render(request, 'account/home.html', context=context)

