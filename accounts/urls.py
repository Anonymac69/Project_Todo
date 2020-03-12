from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name='register'),
    path('modify_user/', views.edit_user, name='modify'),
    path('password/', views.password, name='password'),
    path('delete/<list_id>', views.delete, name='delete'),
]
