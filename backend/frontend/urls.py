from django.urls import path
from . import views 
from .views import RegisterPage


urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('board/', views.board_view, name='board'),
    path('board/<int:board_id>/', views.list_view, name='board_view'),
    path('edit/<int:board_id>/', views.edit_view, name='board_edit'),
    path('delete/<int:board_id>/', views.delete_view, name='board_delete'),
    path('logout/', views.UserLogoutView.as_view(http_method_names=['get', 'post', 'options']), name='logout'),
    
]
