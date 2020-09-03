from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Accout has been Created {username}')
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {'Form':form}
    return render(request, 'register.html', context)
