from django.shortcuts import redirect, render
from django.views.generic import View
from .form import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

class SignupView(View):
    def get(self, request):
        fm = SignUpForm()
        return render(request, 'core/signup.html', {'form':fm})
    def post(self, request):
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Sign Up Success !")
            return redirect('/signup')
        else:
            return render(request, 'core/signup.html', {'form':fm})