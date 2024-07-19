from django.urls import path
from . import views



urlpatterns = [

    path('', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register_view),
    path('board/', views.board_view, name='board'),
    path('logout/', views.UserLogoutView.as_view(http_method_names = ['get', 'post', 'options']), name='logout'),
]
