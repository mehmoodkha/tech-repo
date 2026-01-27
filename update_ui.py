import os
from pathlib import Path

# Define paths
BASE_DIR = Path.cwd()
CORE_TEMPLATES = BASE_DIR / "core" / "templates" / "core"

# Ensure directories exist
CORE_TEMPLATES.mkdir(parents=True, exist_ok=True)

# --- 1. NEW BASE TEMPLATE (Dark Mode & Modern Nav) ---
base_html = """
<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Nexus | Master the Cloud</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
    
    <style>
        :root {
            --primary-accent: #0d6efd;
            --secondary-accent: #00d4ff; /* KodeKloud-ish Cyan */
            --dark-bg: #13151a; /* Deep dark background */
            --card-bg: #1e222b;
        }
        
        body {
            background-color: var(--dark-bg);
            color: #e0e0e0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Navbar Styling */
        .navbar {
            background-color: #1a1d24 !important;
            border-bottom: 1px solid #2d323e;
            padding: 1rem 0;
        }
        .navbar-brand {
            font-weight: 700;
            letter-spacing: 0.5px;
            color: #fff !important;
        }
        .nav-link {
            color: #b0b3b8 !important;
            font-weight: 500;
            transition: color 0.3s;
        }
        .nav-link:hover, .nav-link.active {
            color: var(--secondary-accent) !important;
        }
        .btn-brand {
            background-color: var(--primary-accent);
            color: white;
            font-weight: 600;
            border: none;
            padding: 0.5rem 1.5rem;
            border-radius: 5px;
            transition: all 0.3s;
        }
        .btn-brand:hover {
            background-color: #0b5ed7;
            transform: translateY(-2px);
        }

        /* Footer */
        footer {
            background-color: #0f1115;
            border-top: 1px solid #2d323e;
            padding: 3rem 0;
            margin-top: 5rem;
        }
    </style>
</head>
<body>

<nav class="navbar navbar-expand-lg sticky-top">
  <div class="container">
    <a class="navbar-brand" href="{% url 'home' %}">
        <i class="bi bi-clouds-fill me-2" style="color: var(--secondary-accent);"></i>DevOps Nexus
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto align-items-center">
            <li class="nav-item"><a class="nav-link" href="#">Learning Paths</a></li>
            <li class="nav-item"><a class="nav-link" href="#">Community</a></li>
            
            {% if user.is_authenticated %}
                <li class="nav-item ms-3">
                    <a class="btn btn-outline-light btn-sm" href="{% url 'dashboard' %}">My Dashboard</a>
                </li>
                <li class="nav-item ms-2">
                    <form action="{% url 'logout' %}" method="post" class="d-inline">
                        {% csrf_token %}
                        <button type="submit" class="btn btn-link nav-link text-danger" style="text-decoration:none;">Logout</button>
                    </form>
                </li>
            {% else %}
                <li class="nav-item ms-3">
                    <a class="nav-link" href="{% url 'login' %}">Login</a>
                </li>
                <li class="nav-item ms-2">
                    <a class="btn btn-brand" href="{% url 'register' %}">Sign Up Free</a>
                </li>
            {% endif %}
        </ul>
    </div>
  </div>
</nav>

<div style="min-height: 80vh;">
    {% block content %}{% endblock %}
</div>

<footer class="text-center text-muted">
    <div class="container">
        <div class="row mb-4">
            <div class="col-md-4 text-start">
                <h5 class="text-white mb-3">DevOps Nexus</h5>
                <p class="small">Master Kubernetes, Docker, and CI/CD with hands-on labs and expert-led courses.</p>
            </div>
            <div class="col-md-2 text-start">
                <h6 class="text-white">Resources</h6>
                <ul class="list-unstyled small">
                    <li><a href="#" class="text-decoration-none text-muted">Blog</a></li>
                    <li><a href="#" class="text-decoration-none text-muted">Cheatsheets</a></li>
                </ul>
            </div>
            <div class="col-md-2 text-start">
                <h6 class="text-white">Community</h6>
                <ul class="list-unstyled small">
                    <li><a href="#" class="text-decoration-none text-muted">Forum</a></li>
                    <li><a href="#" class="text-decoration-none text-muted">Discord</a></li>
                </ul>
            </div>
        </div>
        <div class="border-top border-secondary pt-3">
            <small>&copy; 2024 DevOps Nexus. All rights reserved.</small>
        </div>
    </div>
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

# --- 2. NEW HOME TEMPLATE (KodeKloud Style) ---
home_html = """
{% extends 'core/base.html' %}

{% block content %}
<style>
    /* Hero Section */
    .hero-section {
        padding: 6rem 0;
        background: radial-gradient(circle at top right, #1e2532 0%, #13151a 60%);
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 1.5rem;
    }
    .hero-highlight {
        color: var(--secondary-accent);
    }
    
    /* Stats Bar */
    .stats-bar {
        background-color: #1a1d24;
        border-top: 1px solid #2d323e;
        border-bottom: 1px solid #2d323e;
        padding: 1.5rem 0;
    }
    .stat-item h3 { color: white; font-weight: 700; margin: 0; }
    .stat-item p { color: #8b949e; margin: 0; font-size: 0.9rem; }

    /* Cards */
    .course-card {
        background-color: var(--card-bg);
        border: 1px solid #2d323e;
        border-radius: 12px;
        transition: transform 0.3s, border-color 0.3s;
        height: 100%;
    }
    .course-card:hover {
        transform: translateY(-5px);
        border-color: var(--secondary-accent);
    }
    .icon-box {
        width: 50px;
        height: 50px;
        background: rgba(0, 212, 255, 0.1);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--secondary-accent);
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    .tech-tag {
        font-size: 0.75rem;
        padding: 4px 8px;
        border-radius: 4px;
        background: #2d323e;
        color: #b0b3b8;
        margin-right: 5px;
    }
</style>

<section class="hero-section">
    <div class="container">
        <div class="row align-items-center">
            <div class="col-lg-7">
                <span class="badge bg-secondary bg-opacity-25 text-info mb-3 px-3 py-2 rounded-pill">
                    🚀 New: CKAD 2025 Refresher Course
                </span>
                <h1 class="hero-title text-white">
                    Master DevOps with <br>
                    <span class="hero-highlight">Hands-On Labs</span>
                </h1>
                <p class="lead text-secondary mb-4" style="max-width: 600px;">
                    Stop watching video lectures. Start deploying real infrastructure. 
                    Learn Docker, Kubernetes, Ansible, and Terraform in live environments directly in your browser.
                </p>
                <div class="d-flex gap-3">
                    <a href="{% url 'register' %}" class="btn btn-brand btn-lg px-4">Start Learning Free</a>
                    <a href="#" class="btn btn-outline-light btn-lg px-4">View Learning Paths</a>
                </div>
                <div class="mt-4 text-muted small">
                    <i class="bi bi-check-circle-fill text-success me-1"></i> No credit card required
                    <span class="mx-2">•</span>
                    <i class="bi bi-check-circle-fill text-success me-1"></i> Instant lab access
                </div>
            </div>
            <div class="col-lg-5 d-none d-lg-block text-end">
                 <div class="p-4 rounded-4" style="background: linear-gradient(135deg, #2b303b 0%, #1e222b 100%); border: 1px solid #3e4451;">
                    <div class="text-start font-monospace text-info mb-2">$ kubectl get pods</div>
                    <div class="text-start font-monospace text-white">NAME &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; READY &nbsp;&nbsp; STATUS &nbsp;&nbsp; RESTARTS</div>
                    <div class="text-start font-monospace text-success">nginx-deploy &nbsp; 1/1 &nbsp;&nbsp;&nbsp; Running &nbsp; 0</div>
                    <div class="text-start font-monospace text-success">api-gateway &nbsp;&nbsp; 1/1 &nbsp;&nbsp;&nbsp; Running &nbsp; 0</div>
                    <div class="text-start font-monospace text-secondary mt-2">...</div>
                    <div class="mt-3 text-center">
                        <button class="btn btn-sm btn-primary opacity-75">Launch Terminal</button>
                    </div>
                 </div>
            </div>
        </div>
    </div>
</section>

<section class="stats-bar">
    <div class="container">
        <div class="row text-center g-4">
            <div class="col-md-3 col-6 stat-item">
                <h3>500k+</h3>
                <p>Happy Students</p>
            </div>
            <div class="col-md-3 col-6 stat-item">
                <h3>4.8/5</h3>
                <p>Course Rating</p>
            </div>
            <div class="col-md-3 col-6 stat-item">
                <h3>200+</h3>
                <p>Hands-on Labs</p>
            </div>
            <div class="col-md-3 col-6 stat-item">
                <h3>50+</h3>
                <p>Learning Paths</p>
            </div>
        </div>
    </div>
</section>

<section class="py-5">
    <div class="container">
        <div class="d-flex justify-content-between align-items-end mb-4">
            <div>
                <h2 class="text-white fw-bold">Popular Learning Paths</h2>
                <p class="text-muted mb-0">Structured roadmaps to take you from beginner to expert.</p>
            </div>
            <a href="#" class="text-decoration-none text-info">View all paths <i class="bi bi-arrow-right"></i></a>
        </div>

        <div class="row g-4">
            <div class="col-md-4">
                <div class="course-card p-4">
                    <div class="icon-box">
                        <i class="bi bi-hdd-network"></i>
                    </div>
                    <h4 class="text-white mb-2">DevOps Pre-Requisite</h4>
                    <p class="text-muted small mb-3">Master the basics of Linux, Networking, and Git before diving into complex tools.</p>
                    <div class="mb-4">
                        <span class="tech-tag">Linux</span>
                        <span class="tech-tag">Git</span>
                        <span class="tech-tag">Bash</span>
                    </div>
                    <a href="#" class="btn btn-outline-light w-100 btn-sm">Start Path</a>
                </div>
            </div>

            <div class="col-md-4">
                <div class="course-card p-4">
                    <div class="icon-box" style="color: #3771e0; background: rgba(55, 113, 224, 0.1);">
                        <i class="bi bi-box-seam"></i>
                    </div>
                    <h4 class="text-white mb-2">Docker for Beginners</h4>
                    <p class="text-muted small mb-3">Learn how to build, ship, and run applications using containers.</p>
                    <div class="mb-4">
                        <span class="tech-tag">Containers</span>
                        <span class="tech-tag">Images</span>
                    </div>
                    <a href="#" class="btn btn-outline-light w-100 btn-sm">Start Path</a>
                </div>
            </div>

            <div class="col-md-4">
                <div class="course-card p-4">
                    <div class="icon-box" style="color: #326ce5; background: rgba(50, 108, 229, 0.1);">
                        <i class="bi bi-diagram-3"></i>
                    </div>
                    <h4 class="text-white mb-2">Kubernetes Administrator</h4>
                    <p class="text-muted small mb-3">Prepare for the CKA exam with deep dives into architecture and troubleshooting.</p>
                    <div class="mb-4">
                        <span class="tech-tag">K8s</span>
                        <span class="tech-tag">Cluster</span>
                    </div>
                    <a href="#" class="btn btn-outline-light w-100 btn-sm">Start Path</a>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="py-5 bg-darker" style="background-color: #16191f;">
    <div class="container text-center">
        <h2 class="text-white mb-5">Why learn with us?</h2>
        <div class="row g-5">
            <div class="col-md-4">
                <i class="bi bi-terminal-fill fs-1 text-info mb-3"></i>
                <h5 class="text-white">Browser-Based Labs</h5>
                <p class="text-muted">No installations required. Access real environments instantly from your browser.</p>
            </div>
            <div class="col-md-4">
                <i class="bi bi-trophy-fill fs-1 text-warning mb-3"></i>
                <h5 class="text-white">Gamified Learning</h5>
                <p class="text-muted">Earn points, badges, and certificates as you complete challenges.</p>
            </div>
            <div class="col-md-4">
                <i class="bi bi-people-fill fs-1 text-success mb-3"></i>
                <h5 class="text-white">Active Community</h5>
                <p class="text-muted">Join thousands of engineers helping each other debug and learn.</p>
            </div>
        </div>
    </div>
</section>
{% endblock %}
"""

# --- 3. EXECUTE UPDATES ---
def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Updated: {path}")

def main():
    print("Updating UI to 'KodeKloud' Dark Mode style...")
    
    # Overwrite Base Template
    write_file(CORE_TEMPLATES / "base.html", base_html)
    
    # Overwrite Home Template
    write_file(CORE_TEMPLATES / "home.html", home_html)
    
    print("\n✅ UI Update Complete!")
    print("Refresh your browser to see the changes.")

if __name__ == "__main__":
    main()