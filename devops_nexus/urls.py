from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from core import views as core_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', core_views.home, name='home'),
    path('dashboard/', core_views.dashboard, name='dashboard'),
    path('dashboard/submit-feedback/', core_views.submit_feedback, name='submit_feedback'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
    # Admin student management (must come before Django admin)
    path('manage/students/', core_views.admin_students, name='admin_students'),
    path('manage/students/<int:user_id>/', core_views.admin_student_dashboard, name='admin_student_dashboard'),
    path('manage/students/<int:user_id>/update-progress/', core_views.admin_update_progress, name='admin_update_progress'),
    
    # Django admin (must be last)
    path('admin/', admin.site.urls),
]
