from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register, name="register"),
    path('user/', views.user_main, name="user_main"),
]
