from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in user immediately after registration
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            request.user.email = email
            request.user.save()
            message = "Profile updated successfully."
        else:
            message = "Email cannot be empty."
        return render(request, 'blog/profile.html', {'message': message})
    return render(request, 'blog/profile.html')
