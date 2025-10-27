from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('places:place_list')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
