# User_service/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('User_crud.urls')),  # 회원가입 URL 연결
    path('', include('User_crud.urls')),  # 홈 URL로 사용
]
