from django.shortcuts import render, redirect
from .forms import LoginForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required


@login_required
def user_main(request):
    user = request.user
    posts = user.write_posts.all()
    posts_count = user.write_posts.count()
    
    context = {
        'user': user,
        'posts': posts,
        'posts_count': posts_count
    }
    return render(request, "user/user_main.html", context)
    
    
def login_view(request):
    if request.method == "POST":
        print("로그인 포스트요청!")
        form = LoginForm(request.POST)
        if form.is_valid():
            print("로그인 폼 valid!")
            id = form.cleaned_data['id']
            password = form.cleaned_data['password']
            # 사용자 인증
            user = authenticate(request, username=id, password=password)
            print(user)
            if user is not None:
                # 로그인 처리
                login(request, user)
                return redirect('post:main')
            else:
                # 인증 실패
                print("인증 실패:",)
                form.add_error(None, "Invalid ID or Password")
                context = {
                    'form': form,
                }
                return render(request, "user/login.html", context)
        else:
            print("로그인 폼 invalid!")
    form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, "user/login.html", context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("post:main")

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('user:login')  # 회원가입 후 리디렉션할 URL
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'user/register.html', {'form': form})