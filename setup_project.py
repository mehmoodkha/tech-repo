import os
import sys
import subprocess
import shutil
from pathlib import Path

# --- Configuration ---
PROJECT_NAME = "devops_nexus"
APPS = ["core", "users"]
VENV_NAME = "venv"

# Determine OS for venv python path
if sys.platform == "win32":
    VENV_PYTHON = os.path.join(VENV_NAME, "Scripts", "python.exe")
else:
    VENV_PYTHON = os.path.join(VENV_NAME, "bin", "python")

def print_step(message):
    print(f"\n\033[92m[STEP] {message}\033[0m")

def run_command(command, cwd=None, use_venv=True):
    """Runs a shell command. If use_venv is True, prepends the venv python path."""
    if use_venv:
        # If the command starts with 'python', replace it with the venv python
        if command.startswith("python"):
            command = command.replace("python", VENV_PYTHON, 1)
        # If it's pip, use the venv python -m pip
        elif command.startswith("pip"):
            command = command.replace("pip", f"{VENV_PYTHON} -m pip", 1)
    
    print(f"Executing: {command}")
    try:
        subprocess.check_call(command, shell=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"\033[91mError executing command: {command}\033[0m")
        sys.exit(1)

def write_file(path, content):
    """Writes content to a file, creating directories if needed."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Created file: {path}")

# --- File Contents ---

SETTINGS_CONTENT = f"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-dev-key'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{PROJECT_NAME}.urls'

TEMPLATES = [
    {{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {{
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        }},
    }},
]

WSGI_APPLICATION = '{PROJECT_NAME}.wsgi.application'

DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }}
}}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

# Custom Auth
AUTH_USER_MODEL = 'users.CustomUser'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
"""

URLS_MAIN_CONTENT = """
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from core import views as core_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('dashboard/', core_views.dashboard, name='dashboard'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
"""

MODELS_USER_CONTENT = """
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    is_student = models.BooleanField(default=True)
    bio = models.TextField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
"""

MANAGERS_USER_CONTENT = """
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
"""

FORMS_USER_CONTENT = """
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)
"""

VIEWS_USER_CONTENT = """
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})
"""

VIEWS_CORE_CONTENT = """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')
"""

TEMPLATE_BASE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Nexus</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
  <div class="container">
    <a class="navbar-brand" href="{% url 'home' %}">DevOps Nexus</a>
    <div class="navbar-nav ms-auto">
        {% if user.is_authenticated %}
            <a class="nav-link" href="{% url 'dashboard' %}">Dashboard</a>
            <form action="{% url 'logout' %}" method="post" class="d-inline">
                {% csrf_token %}
                <button type="submit" class="btn btn-link nav-link">Logout</button>
            </form>
        {% else %}
            <a class="nav-link" href="{% url 'login' %}">Login</a>
            <a class="nav-link btn btn-primary text-white ms-2" href="{% url 'register' %}">Sign Up</a>
        {% endif %}
    </div>
  </div>
</nav>
<div class="container">
    {% block content %}{% endblock %}
</div>
</body>
</html>
"""

TEMPLATE_HOME = """
{% extends 'core/base.html' %}
{% block content %}
<div class="p-5 mb-4 bg-white rounded-3 shadow-sm text-center">
    <h1 class="display-5 fw-bold">Welcome to DevOps Nexus</h1>
    <p class="col-md-8 fs-4 mx-auto">Master CI/CD and Kubernetes.</p>
    <a class="btn btn-primary btn-lg" href="{% url 'register' %}">Join Now</a>
</div>
{% endblock %}
"""

TEMPLATE_DASHBOARD = """
{% extends 'core/base.html' %}
{% block content %}
<h2>Welcome, {{ user.email }}</h2>
<p>This is your protected dashboard.</p>
{% endblock %}
"""

TEMPLATE_LOGIN = """
{% extends 'core/base.html' %}
{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card shadow-sm p-4">
            <h3 class="text-center">Login</h3>
            <form method="POST">
                {% csrf_token %}
                <div class="mb-3">
                    <label>Email</label>
                    <input type="text" name="username" class="form-control" required>
                </div>
                <div class="mb-3">
                    <label>Password</label>
                    <input type="password" name="password" class="form-control" required>
                </div>
                <button type="submit" class="btn btn-dark w-100">Login</button>
            </form>
        </div>
    </div>
</div>
{% endblock %}
"""

TEMPLATE_REGISTER = """
{% extends 'core/base.html' %}
{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card shadow-sm p-4">
            <h3 class="text-center">Register</h3>
            <form method="POST">
                {% csrf_token %}
                {{ form.as_p }}
                <button type="submit" class="btn btn-primary w-100">Sign Up</button>
            </form>
        </div>
    </div>
</div>
{% endblock %}
"""

# --- Execution ---

def main():
    print_step("Initializing Project Setup...")

    # 1. Create Virtual Environment
    if not os.path.exists(VENV_NAME):
        print_step("Creating Virtual Environment...")
        subprocess.check_call([sys.executable, "-m", "venv", VENV_NAME])
    else:
        print("Virtual environment already exists.")

    # 2. Install Django
    print_step("Installing Django...")
    run_command("pip install django")

    # 3. Create Django Project
    if not os.path.exists(PROJECT_NAME):
        print_step(f"Creating Django Project: {PROJECT_NAME}")
        # CHANGED: We now use `python -m django` instead of `django-admin`
        # This ensures we use the version inside the venv
        run_command(f"python -m django startproject {PROJECT_NAME} .")
    else:
        print(f"Project directory {PROJECT_NAME} already exists, skipping creation.")

    # 4. Create Apps
    print_step("Creating Apps (core, users)...")
    for app in APPS:
        if not os.path.exists(app):
            run_command(f"python manage.py startapp {app}")

    # 5. Overwrite Files with Custom Code
    print_step("Writing Source Code Files...")
    
    # Paths are relative to the script location
    files_to_create = {
        f"{PROJECT_NAME}/settings.py": SETTINGS_CONTENT,
        f"{PROJECT_NAME}/urls.py": URLS_MAIN_CONTENT,
        "users/models.py": MODELS_USER_CONTENT,
        "users/managers.py": MANAGERS_USER_CONTENT,
        "users/forms.py": FORMS_USER_CONTENT,
        "users/views.py": VIEWS_USER_CONTENT,
        "core/views.py": VIEWS_CORE_CONTENT,
        "core/templates/core/base.html": TEMPLATE_BASE,
        "core/templates/core/home.html": TEMPLATE_HOME,
        "core/templates/core/dashboard.html": TEMPLATE_DASHBOARD,
        "users/templates/users/login.html": TEMPLATE_LOGIN,
        "users/templates/users/register.html": TEMPLATE_REGISTER,
    }

    for path, content in files_to_create.items():
        write_file(path, content)

    # 6. Database Migration
    print_step("Migrating Database...")
    # Delete db.sqlite3 if it exists to avoid conflicts with custom user model swaps
    if os.path.exists("db.sqlite3"):
        os.remove("db.sqlite3")
        print("Removed old db.sqlite3")
        
    run_command("python manage.py makemigrations users")
    run_command("python manage.py makemigrations core") 
    run_command("python manage.py makemigrations") 
    run_command("python manage.py migrate")

    # 7. Final Message
    print_step("SETUP COMPLETE!")
    print("\nTo run your website, execute the following commands in your terminal:")
    if sys.platform == "win32":
        print(f"  {VENV_NAME}\\Scripts\\activate")
    else:
        print(f"  source {VENV_NAME}/bin/activate")
    print("  python manage.py runserver")
    print("\nThen open your browser to http://127.0.0.1:8000/")

if __name__ == "__main__":
    main()