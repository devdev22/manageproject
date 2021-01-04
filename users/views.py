from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
#be.az
def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account created Successfully for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request, 'users/register.html', context)
