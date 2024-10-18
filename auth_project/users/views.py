from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from .forms import CustomUserCreationForm  # Make sure to import your custom form


# # View for user registration
# class RegisterView(View):
#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, 'register.html', {'form': form})

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Log the user in after registration
#             return redirect('login')  # Redirect to home after registration
#         return render(request, 'register.html', {'form': form})

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()  # Use your custom form
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('login')  # Redirect to login after registration
        return render(request, 'register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')  # Get username from POST data
        password = request.POST.get('password')  # Get password from POST data

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

@login_required  # Ensure the user is logged in
def home_view(request):
    return render(request, 'home.html', {'user': request.user})


# View for user logout
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout



def landing_view(request):
    return redirect('register')  # Redirect to the registration page
