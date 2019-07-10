from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()#
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required#decorator, sluży do pożyczenia funkcji z innej funkcji, pozwala na to, że tylko zalogowani userzy mogą zobaczyć profile
def profile(request):
    return render(request, 'users/profile.html')
