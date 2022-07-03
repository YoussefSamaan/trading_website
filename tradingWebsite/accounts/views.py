from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from stocks.models import Portfolio

from .loggedin_restriction import loggedin_restriction
from stocks.login_required import login_required


@loggedin_restriction
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(
                request, ("there was an error loggin in. Try again."))
            return redirect("login")
    else:
        return render(request, 'accounts/login.html', {})


@loggedin_restriction
def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            user_profile = Portfolio(user=user, money_left=100000)
            user_profile.save()
            login(request, user)
            messages.success(request, 'Welcome to the trading website')
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/sign_up.html', context)


@login_required
def delete_user(request):
    user = User.objects.get(username=request.user)
    user.delete()
    messages.success(request, "Your account has been deleted.")
    return redirect("front_page")
