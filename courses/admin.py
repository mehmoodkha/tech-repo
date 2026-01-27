from django.contrib import admin
from .models import Course, Enrollment, StudentProgress, Feedback

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
