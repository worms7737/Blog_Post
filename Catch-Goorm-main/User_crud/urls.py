from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home_view, name='home'),
    path('update/', views.update_view, name='update'),
    path('delete/', views.delete_view, name='delete'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
