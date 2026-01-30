from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from core import views as core_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', core_views.home, name='home'),
    path('learning-paths/', core_views.learning_paths, name='learning_paths'),
    path('dashboard/', core_views.dashboard, name='dashboard'),
    path('dashboard/submit-feedback/', core_views.submit_feedback, name='submit_feedback'),
    
    # Course enrollment and progress
    path('enroll/<int:course_id>/', core_views.enroll_course, name='enroll_course'),
    path('enrollment/<int:enrollment_id>/update-progress/', core_views.update_enrollment_progress, name='update_enrollment_progress'),
    
    # Quiz URLs
    path('quiz/', core_views.quiz_hub, name='quiz_hub'),
    path('quiz/<int:quiz_id>/', core_views.quiz_detail, name='quiz_detail'),
    path('quiz/attempt/<int:attempt_id>/submit/', core_views.submit_quiz, name='submit_quiz'),
    path('quiz/attempt/<int:attempt_id>/results/', core_views.quiz_results, name='quiz_results'),
    
    # Authentication
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
    # Admin student management (must come before Django admin)
    path('manage/students/', core_views.admin_students, name='admin_students'),
    path('manage/students/<int:user_id>/', core_views.admin_student_dashboard, name='admin_student_dashboard'),
    path('manage/students/<int:user_id>/update-progress/', core_views.admin_update_progress, name='admin_update_progress'),
    path('manage/students/enrollment/<int:enrollment_id>/update-progress/', core_views.admin_update_enrollment_progress, name='admin_update_enrollment_progress'),
    
    # Django admin (must be last)
    path('admin/', admin.site.urls),
]
