from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from courses.models import Enrollment, StudentProgress, Feedback
import json

User = get_user_model()

def home(request):
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    # Fetch all enrollments for the logged-in user
    user_enrollments = Enrollment.objects.filter(user=request.user)
    
    # Get or create progress for the user
    progress, created = StudentProgress.objects.get_or_create(user=request.user)
    
    # Serialize topics_data to JSON string for template
    topics_json = json.dumps(progress.topics_data) if progress.topics_data else '{}'
    
    # Get user's feedbacks
    user_feedbacks = Feedback.objects.filter(user=request.user)
    
    context = {
        'enrollments': user_enrollments,
        'progress': progress,
        'topics_json': topics_json,
        'user_feedbacks': user_feedbacks,
    }
    return render(request, 'core/dashboard.html', context)

@login_required
@require_POST
def submit_feedback(request):
    """Submit student feedback"""
    message = request.POST.get('message', '').strip()
    rating = request.POST.get('rating', 5)
    
    if message:
        Feedback.objects.create(
            user=request.user,
            message=message,
            rating=int(rating)
        )
        messages.success(request, 'Thank you for your feedback!')
    else:
        messages.error(request, 'Please provide a feedback message.')
    
    return redirect('dashboard')

@staff_member_required
def admin_students(request):
    """Admin view to see all students"""
    students = User.objects.filter(is_staff=False).order_by('-date_joined')
    
    # Get latest feedbacks
    latest_feedbacks = Feedback.objects.select_related('user').order_by('-created_at')[:10]
    
    context = {
        'students': students,
        'latest_feedbacks': latest_feedbacks,
    }
    return render(request, 'core/admin_students.html', context)

@staff_member_required
def admin_student_dashboard(request, user_id):
    """Admin view to see and edit a specific student's dashboard"""
    student = get_object_or_404(User, id=user_id, is_staff=False)
    user_enrollments = Enrollment.objects.filter(user=student)
    progress, created = StudentProgress.objects.get_or_create(user=student)
    
    # Serialize topics_data to JSON string for template
    topics_json = json.dumps(progress.topics_data) if progress.topics_data else '{}'
    
    context = {
        'student': student,
        'enrollments': user_enrollments,
        'progress': progress,
        'topics_json': topics_json,
        'is_admin_view': True,
    }
    return render(request, 'core/admin_student_dashboard.html', context)


@staff_member_required
@require_POST
def admin_update_progress(request, user_id):
    """API endpoint for admin to update student progress"""
    student = get_object_or_404(User, id=user_id, is_staff=False)
    progress, created = StudentProgress.objects.get_or_create(user=student)
    
    try:
        data = json.loads(request.body)
        topics_data = data.get('topics_data')
        total_fees = data.get('total_fees')
        paid_amount = data.get('paid_amount')
        
        if topics_data is not None:
            progress.topics_data = topics_data
        
        if total_fees is not None:
            progress.total_fees = float(total_fees)
        
        if paid_amount is not None:
            progress.paid_amount = float(paid_amount)
        
        progress.save()
        
        return JsonResponse({
            'success': True,
            'completed': progress.get_completed_count(),
            'percentage': progress.get_completion_percentage(),
            'fee_percentage': progress.get_fee_percentage(),
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)
