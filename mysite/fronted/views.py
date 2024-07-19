from django.shortcuts import redirect, render

# Create your views here.
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView

# def login_view(request):
#     return render(request, 'auth/login.html')

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('board')

class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        return redirect('login')
    

def register_view(request):
    return render(request, 'auth/register.html')

@login_required
def board_view(request):
    return render(request, 'board/index.html')