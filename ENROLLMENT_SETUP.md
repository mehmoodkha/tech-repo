# Enrollment Feature Setup Instructions

This document explains the enrollment functionality that has been implemented.

## Features Implemented

1. **Dynamic Course Enrollment from Home Page**
   - When users click "Start Path" on any learning path, they can enroll in courses
   - If not logged in, users are redirected to login page with a redirect back to enrollment
   - If already enrolled, shows "Enrolled - Go to Dashboard" button
   - If logged in but not enrolled, shows "Enroll Now" button

2. **Student Dashboard Shows Enrolled Courses**
   - All enrolled courses are displayed in the student dashboard
   - Shows course title, duration, price
   - Shows payment status (Paid, Pending, Failed)
   - Shows progress bar for paid courses
   - Shows payment prompt for pending courses

3. **Admin Dashboard Shows Student Enrollments**
   - Admin can see all enrolled courses for each student
   - Shows course details and payment status
   - Integrated into the existing admin student management view

## Setup Steps

### 1. Create Sample Courses

First, populate the database with sample courses:

```bash
python setup_courses.py
```

This will create 9 courses:
- DevOps Pre-Requisite
- Docker for Beginners
- Kubernetes Administrator (CKA)
- Jenkins CI/CD Pipeline
- Terraform Infrastructure as Code
- Ansible Automation
- AWS Cloud Practitioner
- Python for DevOps
- Site Reliability Engineering (SRE)

### 2. Start the Development Server

```bash
python manage.py runserver
```

### 3. Test the Enrollment Flow

1. **Register a new student account** (if you don't have one):
   - Go to http://127.0.0.1:8000/register/
   - Fill in the registration form
   - Login with your credentials

2. **Enroll in a course**:
   - Go to the home page: http://127.0.0.1:8000/
   - Click "Enroll Now" on any learning path card
   - You'll be enrolled and redirected to your dashboard

3. **View your enrollments**:
   - Go to your dashboard: http://127.0.0.1:8000/dashboard/
   - Scroll down to see "My Enrolled Courses" section
   - You should see all courses you enrolled in

4. **Admin View** (requires staff/superuser account):
   - Login to admin portal
   - Go to "Manage Students"
   - Click on any student
   - Scroll down to see their enrolled courses

## Technical Details

### Models Used
- `Course`: Stores course information (title, description, price, duration)
- `Enrollment`: Links users to courses with payment status
- `StudentProgress`: Tracks RHCSA progress and fee payments

### Views Added
- `enroll_course(request, course_id)`: Handles enrollment logic
- `home(request)`: Updated to pass courses to template
- `dashboard(request)`: Already passes enrollments
- `admin_student_dashboard(request, user_id)`: Already passes enrollments

### Templates Updated
- `core/templates/core/home.html`: Dynamic enrollment buttons
- `core/templates/core/dashboard.html`: Already shows enrollments
- `core/templates/core/admin_student_dashboard.html`: Already shows enrollments

### URLs Added
- `/enroll/<course_id>/`: Enrollment endpoint

### Custom Template Filter
- `filter_by_course`: Checks if user is enrolled in a specific course

## Payment Flow (For Future Enhancement)

Currently, enrollments are created with `PENDING` payment status. You can:

1. Manually update payment status in Django admin
2. Integrate a payment gateway (Stripe, Razorpay, etc.)
3. Add a "Pay Now" button that processes payments

## Notes

- Enrollments are unique per user-course combination (can't enroll twice)
- Login is required to enroll in courses
- Enrolled courses with PENDING status show "Pay Now" button
- Enrolled courses with PAID status show progress tracking
- Admin can view and manage all student enrollments
