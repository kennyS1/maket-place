from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.userLogout, name='logout'),  # 更改为重定向到主页
    path('profile/edit/', views.editprofile, name='editprofile'),
    path('profile/', views.profile, name='profile'),  # 如果你还没写，可以加这个
]
