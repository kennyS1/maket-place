from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
        
    else:
        form = SignupForm()
        
    return render(request, 'signup.html', {'form': form})

# about me view
@login_required  # 确保只有登录用户才能访问
def profile(request):
    user = request.user  # 获取当前登录用户
    context = {
        'user': user,  # 传递用户对象到模板
    }
    return render(request, 'profile.html', context)


# Create your views here.
def userLogout(request):
    logout(request)
    return redirect('home')  # 跳转到主页



#profile
# 修改个人信息的视图函数
@login_required
def editprofile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # 修改完回到个人页面
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'editprofile.html', {'form': form})
    