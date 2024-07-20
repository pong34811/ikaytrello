from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Board

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
    #create a new board
    if request.method == "POST":
        board_name = request.POST.get('board_name')
        if board_name:
            board = Board.objects.create(
                board_name=board_name,
                user=request.user,
                created_by=request.user,
                updated_by=request.user,
            )
            return redirect('board')
    #ดึงข้อมูล ในเเสดงหน้า page : board/index.html
    boards = Board.objects.filter(user=request.user)
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

    #ดึงข้อมูล ในเเสดงหน้า page : board/view.html
    # boards = Board.objects.filter(user=request.user)
    # return render(request, 'board/index.html', {"boards": boards})  # แก้ไขชื่อชั้นต้นให้ตรงกัน

    # return redirect('board')  # แก้ไขชื่อฟังชั่นให้ตรงกัน

    # return render(request, 'board/index.html', {"boards": boards})  # แก้ไขชื่อชั้นต้นให้ตรงก
    
@login_required
def list_view(request, board_id):  # แก้ไขชื่อพารามิเตอร์ให้ตรงกัน
    board = Board.objects.get(id=board_id)
    return render(request, 'board/view.html', {"board": board})

