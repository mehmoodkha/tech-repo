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

class StudentProgress(models.Model):
    """Track RHCSA/RHCE topic progress for each student"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rhcsa_progress')
    topics_data = models.JSONField(default=dict, blank=True)  # Store {topic_index: True/False}
    last_updated = models.DateTimeField(auto_now=True)
    
    # Fee status
    total_fees = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"{self.user.email} - Progress"
    
    def get_completion_percentage(self):
        if not self.topics_data:
            return 0
        completed = sum(1 for val in self.topics_data.values() if val)
        total = 30  # Total RHCSA topics
        return round((completed / total) * 100)
    
    def get_completed_count(self):
        if not self.topics_data:
            return 0
        return sum(1 for val in self.topics_data.values() if val)
    
    def get_fee_percentage(self):
        if self.total_fees <= 0:
            return 0
        return round((self.paid_amount / self.total_fees) * 100)
    
    def get_remaining_fees(self):
        return max(0, self.total_fees - self.paid_amount)

class Feedback(models.Model):
    """Student feedback and testimonials"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feedbacks')
    message = models.TextField()
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)  # Admin can approve for display
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.email} - {self.rating} stars"
