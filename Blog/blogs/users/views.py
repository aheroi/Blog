from django.shortcuts import redirect, render
# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """register a new user"""
    if request.method != 'POST':
        # displays empty form for registration
        form = UserCreationForm()
    else:
        # processing completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # log in and redirect to home page
            login(request, new_user)
            return redirect('blogs_first:index')

    # display an empty or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
    