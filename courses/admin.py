from django.contrib import admin
from .models import Course, Enrollment, StudentProgress, Feedback, Quiz, Question, QuizAttempt, QuizAnswer

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'duration')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'payment_status', 'date_enrolled')
    list_filter = ('payment_status', 'course')
    search_fields = ('user__email', 'course__title')

@admin.register(StudentProgress)
class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_completed_count', 'get_completion_percentage', 'last_updated')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    readonly_fields = ('last_updated',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'rating', 'created_at')
    search_fields = ('user__email', 'message')
    readonly_fields = ('created_at',)
    actions = ['approve_feedback']
    
    def approve_feedback(self, request, queryset):
        queryset.update(is_approved=True)
    approve_feedback.short_description = "Approve selected feedback"


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    fields = ('question_text', 'choice_a', 'choice_b', 'choice_c', 'choice_d', 'correct_answer', 'order', 'is_active')


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('topic', 'difficulty', 'get_questions_count', 'is_active', 'created_at')
    list_filter = ('topic', 'difficulty', 'is_active')
    search_fields = ('title', 'description')
    inlines = [QuestionInline]
    readonly_fields = ('created_at',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'question_text_short', 'order', 'is_active')
    list_filter = ('quiz__topic', 'quiz__difficulty', 'is_active')
    search_fields = ('question_text', 'answer')
    list_editable = ('order', 'is_active')
    
    def question_text_short(self, obj):
        return obj.question_text[:100] + '...' if len(obj.question_text) > 100 else obj.question_text
    question_text_short.short_description = 'Question'


class QuizAnswerInline(admin.TabularInline):
    model = QuizAnswer
    extra = 0
    readonly_fields = ('question', 'user_answer', 'is_correct', 'answered_at')
    can_delete = False


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'total_questions', 'get_percentage', 'get_time_formatted', 'is_completed', 'started_at')
    list_filter = ('quiz__topic', 'quiz__difficulty', 'is_completed', 'started_at')
    search_fields = ('user__email', 'quiz__title')
    readonly_fields = ('started_at', 'completed_at')
    inlines = [QuizAnswerInline]
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'quiz')


@admin.register(QuizAnswer)
class QuizAnswerAdmin(admin.ModelAdmin):
    list_display = ('attempt', 'question', 'is_correct', 'answered_at')
    list_filter = ('is_correct', 'answered_at')
    search_fields = ('attempt__user__email', 'question__question_text')
    readonly_fields = ('answered_at',)
