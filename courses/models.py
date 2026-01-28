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


class Quiz(models.Model):
    """Quiz topics with difficulty levels"""
    TOPIC_CHOICES = [
        ('LINUX', 'Linux'),
        ('CLOUD', 'Cloud'),
        ('DOCKER', 'Docker'),
        ('ANSIBLE', 'Ansible'),
        ('TERRAFORM', 'Terraform'),
        ('JENKINS', 'Jenkins'),
        ('DEVOPS', 'DevOps'),
        ('SRE', 'SRE'),
        ('PYTHON', 'Python'),
    ]
    
    DIFFICULTY_CHOICES = [
        ('BASIC', 'Basic'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
    ]
    
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    difficulty = models.CharField(max_length=15, choices=DIFFICULTY_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['topic', 'difficulty']
        unique_together = ('topic', 'difficulty')
    
    def __str__(self):
        return f"{self.get_topic_display()} - {self.get_difficulty_display()}"
    
    def get_questions_count(self):
        return self.questions.count()


class Question(models.Model):
    """Questions for each quiz"""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    
    # Multiple choice options (stored as JSON array)
    choice_a = models.CharField(max_length=500, blank=True, default='')
    choice_b = models.CharField(max_length=500, blank=True, default='')
    choice_c = models.CharField(max_length=500, blank=True, default='')
    choice_d = models.CharField(max_length=500, blank=True, default='')
    
    # Correct answer (A, B, C, or D)
    correct_answer = models.CharField(max_length=1, choices=[
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')
    ], default='A')
    
    # Legacy field for compatibility
    answer = models.TextField(blank=True, help_text="Explanation or legacy answer")
    
    order = models.IntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['quiz', 'order']
    
    def __str__(self):
        return f"{self.quiz} - Q{self.order}"
    
    def get_correct_choice_text(self):
        """Return the text of the correct answer"""
        choices = {
            'A': self.choice_a,
            'B': self.choice_b,
            'C': self.choice_c,
            'D': self.choice_d
        }
        return choices.get(self.correct_answer, '')


class QuizAttempt(models.Model):
    """Track student quiz attempts and performance"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quiz_attempts')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempts')
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(default=0, help_text="Number of correct answers")
    total_questions = models.IntegerField(default=0)
    time_spent = models.IntegerField(default=0, help_text="Time spent in seconds")
    is_completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-started_at']
    
    def __str__(self):
        return f"{self.user.email} - {self.quiz} - {self.started_at.strftime('%Y-%m-%d')}"
    
    def get_percentage(self):
        if self.total_questions == 0:
            return 0
        return round((self.score / self.total_questions) * 100, 1)
    
    def get_time_formatted(self):
        """Return time in MM:SS format"""
        minutes = self.time_spent // 60
        seconds = self.time_spent % 60
        return f"{minutes:02d}:{seconds:02d}"


class QuizAnswer(models.Model):
    """Track individual answers in a quiz attempt"""
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.TextField(blank=True)
    is_correct = models.BooleanField(default=False)
    answered_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('attempt', 'question')
    
    def __str__(self):
        return f"{self.attempt} - Q{self.question.order}"
