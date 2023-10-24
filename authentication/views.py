from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create the user object without saving it to the database yet
            password = form.cleaned_data['password1']  # Get the user's password from the form
            user.set_password(password)  # Use set_password to securely hash the password
            user.save()  # Save the user to the database
            login(request, user)  # Automatically log the user in after registration
            return redirect('task_manager:task_list')  # Redirect to a page after successful registration
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
