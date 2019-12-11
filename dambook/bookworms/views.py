from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            msg = 'Account created for {}!'.format(username)
            messages.success(request, msg)
            return redirect('library-home')
    else:
        form = UserCreationForm()
    return render(request, 'bookworms/register.html', {'form': form}) 