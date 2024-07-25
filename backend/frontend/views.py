from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
from .models import Board ,models
import json



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
@csrf_exempt
def board_view(request):
    if request.method == "POST":
        if request.POST.get('board_name'):
            # Create a new board
            board_name = request.POST.get('board_name')
            if board_name:
                max_order = Board.objects.filter(user=request.user).aggregate(models.Max('order'))['order__max'] or 0
                board = Board.objects.create(
                    board_name=board_name,
                    user=request.user,
                    created_by=request.user,
                    updated_by=request.user,
                    order=max_order + 1
                )
                return redirect('board')
        
        elif request.content_type == "application/json":
            # Update board order
            data = json.loads(request.body)
            board_ids = data.get('board_ids', [])

            for index, board_id in enumerate(board_ids):
                board = Board.objects.get(id=board_id)
                board.order = index
                board.save()

            # Redirect to the same page
            return redirect('board')

    # Retrieve and display boards ordered by `order`
    boards = Board.objects.filter(user=request.user).order_by('order')
    return render(request, 'board/index.html', {"boards": boards})

@login_required
def edit_view(request, board_id):
    board = Board.objects.get(id=board_id)
    if request.method == "POST":
        board_name = request.POST.get('board_name')
        if board_name:
            board.board_name = board_name
            board.updated_by = request.user
            board.save()
            return redirect('board')
    return render(request, 'board/edit_modal.html', {"board": board})

@login_required
def delete_view(request, board_id):
    board = Board.objects.get(id=board_id)
    board.delete()
    return redirect('board')

@login_required
def list_view(request, board_id):
    board = Board.objects.get(id=board_id)
    return render(request, 'board/view.html', {"board": board})
