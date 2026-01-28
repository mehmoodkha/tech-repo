from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from courses.models import Enrollment, StudentProgress, Feedback, Quiz, Question, QuizAttempt, QuizAnswer, Course
from django.utils import timezone
from django.db.models import Count, Avg, Q, F, FloatField, ExpressionWrapper
from django.db import models
import json

User = get_user_model()

def home(request):
    # Get available courses with Linux - RHCSA and RHCE first
    linux_course = Course.objects.filter(title__icontains='Linux - RHCSA')
    other_courses = Course.objects.exclude(title__icontains='Linux - RHCSA')
    courses = list(linux_course) + list(other_courses)
    context = {
        'courses': courses
    }
    return render(request, 'core/home.html', context)

def learning_paths(request):
    """Display all available learning paths with Linux - RHCSA and RHCE first"""
    linux_course = Course.objects.filter(title__icontains='Linux - RHCSA')
    other_courses = Course.objects.exclude(title__icontains='Linux - RHCSA')
    courses = list(linux_course) + list(other_courses)
    context = {
        'courses': courses
    }
    return render(request, 'core/learning_paths.html', context)

@login_required
def enroll_course(request, course_id):
    """Enroll student in a course"""
    course = get_object_or_404(Course, id=course_id)
    
    # Check if already enrolled
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user,
        course=course,
        defaults={'payment_status': 'PENDING'}
    )
    
    if created:
        messages.success(request, f'Successfully enrolled in {course.title}!')
    else:
        messages.info(request, f'You are already enrolled in {course.title}.')
    
    return redirect('dashboard')

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
    
    # Quiz statistics
    total_attempts = QuizAttempt.objects.filter(is_completed=True).count()
    
    # Calculate average percentage score
    completed_attempts = QuizAttempt.objects.filter(is_completed=True)
    if completed_attempts.exists():
        total_percentage = sum([
            (attempt.score / attempt.total_questions * 100) if attempt.total_questions > 0 else 0
            for attempt in completed_attempts
        ])
        avg_score = round(total_percentage / completed_attempts.count(), 1)
    else:
        avg_score = 0
    
    # Top performers in quizzes - calculate percentage for each user
    top_quiz_performers = User.objects.filter(
        is_staff=False,
        quiz_attempts__is_completed=True
    ).annotate(
        total_quizzes=Count('quiz_attempts', filter=Q(quiz_attempts__is_completed=True))
    ).distinct()
    
    # Calculate average percentage for each user
    performers_with_avg = []
    for user in top_quiz_performers:
        user_attempts = QuizAttempt.objects.filter(user=user, is_completed=True)
        if user_attempts.exists():
            total_pct = sum([
                (att.score / att.total_questions * 100) if att.total_questions > 0 else 0
                for att in user_attempts
            ])
            avg_pct = total_pct / user_attempts.count()
            user.avg_score = round(avg_pct, 1)
            user.total_quizzes = user_attempts.count()
            performers_with_avg.append(user)
    
    # Sort by average score and take top 5
    top_quiz_performers = sorted(performers_with_avg, key=lambda x: x.avg_score, reverse=True)[:5]
    
    # Recent quiz attempts
    recent_quiz_attempts = QuizAttempt.objects.filter(
        is_completed=True
    ).select_related('user', 'quiz').order_by('-completed_at')[:10]
    
    context = {
        'students': students,
        'latest_feedbacks': latest_feedbacks,
        'total_attempts': total_attempts,
        'avg_score': avg_score,
        'top_quiz_performers': top_quiz_performers,
        'recent_quiz_attempts': recent_quiz_attempts,
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
    
    # Get student's quiz statistics
    quiz_attempts = QuizAttempt.objects.filter(
        user=student,
        is_completed=True
    ).select_related('quiz').order_by('-completed_at')
    
    # Calculate average percentage
    if quiz_attempts.exists():
        total_pct = sum([
            (att.score / att.total_questions * 100) if att.total_questions > 0 else 0
            for att in quiz_attempts
        ])
        avg_percentage = round(total_pct / quiz_attempts.count(), 1)
    else:
        avg_percentage = 0
    
    quiz_stats = {
        'total_attempts': quiz_attempts.count(),
        'avg_percentage': avg_percentage,
        'recent_attempts': quiz_attempts[:5]
    }
    
    context = {
        'student': student,
        'enrollments': user_enrollments,
        'progress': progress,
        'topics_json': topics_json,
        'is_admin_view': True,
        'quiz_stats': quiz_stats,
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


@login_required
def quiz_hub(request):
    """Display all quiz topics with difficulty levels"""
    # Get all quizzes grouped by topic
    quizzes = Quiz.objects.filter(is_active=True).order_by('topic', 'difficulty')
    
    # Get user's quiz history
    user_attempts = QuizAttempt.objects.filter(user=request.user, is_completed=True).select_related('quiz')
    
    # Create a dictionary to store user's best scores for each quiz
    best_scores = {}
    for attempt in user_attempts:
        quiz_id = attempt.quiz.id
        if quiz_id not in best_scores or attempt.get_percentage() > best_scores[quiz_id]:
            best_scores[quiz_id] = attempt.get_percentage()
    
    # Group quizzes by topic
    topics_data = {}
    for quiz in quizzes:
        topic_name = quiz.get_topic_display()
        if topic_name not in topics_data:
            topics_data[topic_name] = {
                'topic_code': quiz.topic,
                'difficulties': {}
            }
        topics_data[topic_name]['difficulties'][quiz.difficulty] = {
            'quiz': quiz,
            'best_score': best_scores.get(quiz.id, 0)
        }
    
    context = {
        'topics_data': topics_data,
    }
    return render(request, 'core/quiz_hub.html', context)


@login_required
def quiz_detail(request, quiz_id):
    """Display quiz questions one at a time"""
    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
    questions = quiz.questions.filter(is_active=True).order_by('order')
    
    if not questions.exists():
        messages.warning(request, 'This quiz has no questions yet.')
        return redirect('quiz_hub')
    
    # Get or create an active attempt
    active_attempt = QuizAttempt.objects.filter(
        user=request.user,
        quiz=quiz,
        is_completed=False
    ).first()
    
    if not active_attempt:
        active_attempt = QuizAttempt.objects.create(
            user=request.user,
            quiz=quiz,
            total_questions=questions.count()
        )
    
    # Get previous attempts for this quiz
    previous_attempts = QuizAttempt.objects.filter(
        user=request.user,
        quiz=quiz,
        is_completed=True
    ).order_by('-completed_at')[:5]
    
    context = {
        'quiz': quiz,
        'questions': questions,
        'attempt': active_attempt,
        'previous_attempts': previous_attempts,
        'questions_json': json.dumps([{
            'id': q.id,
            'question': q.question_text,
            'choices': {
                'A': q.choice_a,
                'B': q.choice_b,
                'C': q.choice_c,
                'D': q.choice_d
            },
            'correct_answer': q.correct_answer,
            'order': q.order
        } for q in questions])
    }
    return render(request, 'core/quiz_detail.html', context)


@login_required
@require_POST
def submit_quiz(request, attempt_id):
    """Submit quiz and calculate score"""
    attempt = get_object_or_404(QuizAttempt, id=attempt_id, user=request.user, is_completed=False)
    
    try:
        data = json.loads(request.body)
        answers = data.get('answers', {})  # {question_id: user_answer}
        time_spent = data.get('time_spent', 0)
        
        score = 0
        questions = attempt.quiz.questions.filter(is_active=True)
        
        # Process each answer
        for question in questions:
            user_answer = answers.get(str(question.id), '').strip().upper()
            
            # Check if answer is correct (compare with correct_answer field)
            is_correct = user_answer == question.correct_answer
            if is_correct:
                score += 1
            
            # Save individual answer
            QuizAnswer.objects.create(
                attempt=attempt,
                question=question,
                user_answer=user_answer,
                is_correct=is_correct
            )
        
        # Update attempt
        attempt.score = score
        attempt.time_spent = time_spent
        attempt.is_completed = True
        attempt.completed_at = timezone.now()
        attempt.save()
        
        return JsonResponse({
            'success': True,
            'score': score,
            'total': attempt.total_questions,
            'percentage': attempt.get_percentage(),
            'time_formatted': attempt.get_time_formatted()
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@login_required
def quiz_results(request, attempt_id):
    """Display detailed quiz results"""
    attempt = get_object_or_404(QuizAttempt, id=attempt_id, user=request.user, is_completed=True)
    answers = attempt.answers.all().select_related('question').order_by('question__order')
    
    context = {
        'attempt': attempt,
        'answers': answers,
    }
    return render(request, 'core/quiz_results.html', context)
