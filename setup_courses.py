import os
from pathlib import Path

# --- Configuration ---
PROJECT_NAME = "devops_nexus"
APP_NAME = "courses"
BASE_DIR = Path.cwd()

# Ensure the app directory exists
APP_DIR = BASE_DIR / APP_NAME
APP_DIR.mkdir(exist_ok=True)
(APP_DIR / "migrations").mkdir(exist_ok=True)
(APP_DIR / "migrations" / "__init__.py").touch()

def write_file(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Created/Updated: {path}")

# --- 1. MODELS (Database Structure) ---
models_content = """
from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text="Price in USD")
    duration = models.CharField(max_length=50, help_text="e.g. '8 Weeks' or '10 Hours'")
    
    def __str__(self):
        return self.title

class Enrollment(models.Model):
    PAYMENT_CHOICES = [
        ('PAID', 'Paid'),
        ('PENDING', 'Pending'),
        ('FAILED', 'Failed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='PENDING')
    date_enrolled = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')  # Prevent double enrollment

    def __str__(self):
        return f"{self.user.email} -> {self.course.title} ({self.payment_status})"
"""

# --- 2. ADMIN (To manage courses) ---
admin_content = """
from django.contrib import admin
from .models import Course, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'duration')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'payment_status', 'date_enrolled')
    list_filter = ('payment_status', 'course')
    search_fields = ('user__email', 'course__title')
"""

# --- 3. VIEWS (Update Dashboard to show real data) ---
# We overwrite core/views.py to fetch data from the new models
core_views_content = """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import Enrollment

def home(request):
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    # Fetch all enrollments for the logged-in user
    user_enrollments = Enrollment.objects.filter(user=request.user)
    
    context = {
        'enrollments': user_enrollments
    }
    return render(request, 'core/dashboard.html', context)
"""

# --- 4. TEMPLATE (Update Dashboard HTML) ---
dashboard_html_content = """
{% extends 'core/base.html' %}

{% block content %}
<div class="row mt-4">
    <div class="col-md-4">
        <div class="card shadow-sm border-0" style="background-color: #1e222b; border: 1px solid #2d323e;">
            <div class="card-body text-center p-4">
                <div class="mb-3">
                    <div style="width: 100px; height: 100px; background-color: #0d6efd; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; margin: 0 auto; font-weight: bold;">
                        {{ user.first_name|first|default:user.email|first|upper }}
                    </div>
                </div>
                <h4 class="text-white mb-1">
                    {% if user.first_name %}{{ user.first_name }} {{ user.last_name }}{% else %}Student{% endif %}
                </h4>
                <p class="text-muted mb-3">{{ user.email }}</p>
                <div class="d-grid">
                    <a href="#" class="btn btn-outline-light btn-sm">Edit Profile</a>
                </div>
            </div>
        </div>
    </div>

    <div class="col-md-8">
        <h3 class="text-white mb-4">My Enrolled Courses</h3>

        {% if enrollments %}
            {% for enrollment in enrollments %}
            <div class="card mb-3 border-0" style="background-color: #1e222b;">
                <div class="card-body">
                    <div class="d-flex justify-content-between align-items-center mb-2">
                        <h5 class="card-title text-white mb-0">{{ enrollment.course.title }}</h5>
                        
                        {% if enrollment.payment_status == 'PAID' %}
                            <span class="badge bg-success">Active / Paid</span>
                        {% elif enrollment.payment_status == 'PENDING' %}
                            <span class="badge bg-warning text-dark">Payment Pending</span>
                        {% else %}
                            <span class="badge bg-danger">Payment Failed</span>
                        {% endif %}
                    </div>
                    
                    <p class="text-muted small mb-2">{{ enrollment.course.duration }} • Price: ${{ enrollment.course.price }}</p>
                    
                    {% if enrollment.payment_status == 'PAID' %}
                        <div class="progress" style="height: 8px; background-color: #2d323e;">
                            <div class="progress-bar bg-info" role="progressbar" style="width: 10%;"></div>
                        </div>
                        <div class="mt-2 text-end text-muted small">10% Complete</div>
                        <a href="#" class="btn btn-sm btn-primary mt-3">Continue Learning</a>
                    {% else %}
                        <div class="alert alert-warning py-2 mt-3 mb-0 small">
                            <i class="bi bi-exclamation-triangle"></i> Access restricted. Please complete payment.
                        </div>
                        <a href="#" class="btn btn-sm btn-success mt-2">Pay Now</a>
                    {% endif %}
                </div>
            </div>
            {% endfor %}
        {% else %}
            <div class="text-center p-5 rounded" style="background-color: #1e222b; border: 1px dashed #2d323e;">
                <h5 class="text-white">No courses yet</h5>
                <p class="text-muted">You haven't enrolled in any courses.</p>
                <a href="/" class="btn btn-primary">Browse Courses</a>
            </div>
        {% endif %}
    </div>
</div>
{% endblock %}
"""

# --- Execution ---
write_file(APP_DIR / "__init__.py", "")
write_file(APP_DIR / "models.py", models_content)
write_file(APP_DIR / "admin.py", admin_content)
write_file(BASE_DIR / "core" / "views.py", core_views_content)
write_file(BASE_DIR / "core" / "templates" / "core" / "dashboard.html", dashboard_html_content)

print("\n[IMPORTANT] Next Steps:")
print("1. Add 'courses' to INSTALLED_APPS in settings.py")
print("2. Run 'python manage.py makemigrations'")
print("3. Run 'python manage.py migrate'")