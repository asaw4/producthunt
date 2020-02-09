from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #return redirect('home')
            return render(request,'home.html')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

#@login_required(redirect_field_name='my_redirect_field')
def home_view(request):

    return render(request,'home.html')
