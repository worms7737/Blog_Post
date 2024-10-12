from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.conf import settings
from .models import User
import re
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                return redirect(next_url if next_url else 'home')
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
        else:
            return render(request, 'login.html', {'error': 'Please fill in all fields'})

    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        password = request.POST['password']
        avatar = request.FILES.get('profile_image')  # 프로필 이미지 처리

        # 유효성 검사
        name_regex = r'^[a-zA-Z가-힣]+$'
        password_regex = r'^(?=.*[a-zA-Z])(?=.*[0-9]).{8,}$'

        if not re.match(name_regex, first_name):
            messages.error(request, "이름은 한글 또는 영어로만 입력할 수 있습니다.")
            return render(request, 'signup.html')

        if not re.match(password_regex, password):
            messages.error(request, "비밀번호는 8자리 이상이며, 영문자와 숫자를 모두 포함해야 합니다.")
            return render(request, 'signup.html')

        # 사용자 생성 및 비밀번호 해시 처리
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            password=password,
            avatar=avatar  # 이미지 필드 처리
        )

        # 회원가입 후 로그인 페이지로 리다이렉트
        return redirect('login')
    return render(request, 'signup.html')

@login_required
def home_view(request):
    return render(request, 'home.html', {'user': request.user})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import User

@login_required
def update_view(request):
    user = get_object_or_404(User, pk=request.user.id)

    if request.method == "POST":
        # 사용자의 이름 및 비밀번호 업데이트
        user.first_name = request.POST.get('first_name', user.first_name)
        if request.POST.get('password'):
            user.password = make_password(request.POST['password'])

        # 프로필 이미지 업데이트
        if request.FILES.get('profile_image'):
            user.avatar = request.FILES['profile_image']

        user.save()

        return redirect('home')

    return render(request, 'update.html', {'user': user})

@login_required
def delete_view(request):
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == "POST":
        user.delete()
        logout(request)
        return redirect('login')
    return render(request, 'delete.html', {'user': user})
