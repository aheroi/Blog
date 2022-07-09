from django.shortcuts import redirect, render
# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



def register(request):
    """register new user"""
    if request.method !='POST':
        # display empty registration form
        form = UserCreationForm()
    else:
        # process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # sign in and redirect to home page
            login(request, new_user)
            return redirect('learning_logs:index')

    # displays an empty or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
    
