from django.shortcuts import render,redirect
from accounts.forms import UserRegistration
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your account has been"
                                     "created successfully")
            return redirect('login')
    else:
        form = UserRegistration()
    dict = {'form': form}
    return render(request, 'accounts/register.html',dict)
