# Quiz Feature Documentation

## Overview
A comprehensive quiz system has been implemented with the following features:

### Key Features

#### 1. **Quiz Hub - 9 Distinct Topics**
- Linux
- Cloud
- Docker
- Ansible
- Terraform
- Jenkins
- DevOps
- SRE
- Python

#### 2. **Difficulty Tiers**
Each topic has three difficulty levels:
- **Basic**: Fundamental concepts
- **Intermediate**: Practical knowledge
- **Advanced**: Expert-level understanding

#### 3. **Interactive Q&A**
- Questions displayed one at a time
- Answer remains hidden until "Show Answer" button is clicked
- Navigation between questions
- Progress indicator showing current position

#### 4. **Results & Metrics**
- Quiz attempts are saved automatically
- Score calculation (correct/total)
- Time tracking
- Performance history
- Previous attempts visible on quiz detail page

#### 5. **Admin Portal Integration**
Admin dashboard shows:
- Total quiz attempts across all students
- Average scores
- Top performers leaderboard
- Recent quiz attempts
- Individual student quiz statistics

## File Structure

```
courses/
  models.py              # Quiz, Question, QuizAttempt, QuizAnswer models
  admin.py               # Admin interface for quiz management

core/
  views.py               # Quiz views (hub, detail, submit, results)
  templates/core/
    quiz_hub.html        # Main quiz selection page
    quiz_detail.html     # Interactive quiz interface
    quiz_results.html    # Detailed results page
    dashboard.html       # Updated with quiz link
    admin_students.html  # Admin view with quiz metrics

devops_nexus/
  urls.py                # Quiz URL patterns

setup_quizzes.py         # Script to populate sample questions
```

## Database Models

### Quiz
- Topic (9 choices)
- Difficulty (3 levels)
- Title and description
- Active status
- Creation timestamp

### Question
- Quiz (foreign key)
- Question text
- Answer
- Order
- Active status

### QuizAttempt
- User (foreign key)
- Quiz (foreign key)
- Score
- Total questions
- Time spent
- Completion status
- Timestamps

### QuizAnswer
- Attempt (foreign key)
- Question (foreign key)
- User answer
- Correctness flag
- Timestamp

## Usage

### For Students

1. **Access Quiz Hub**
   - Click "Take Quiz" button on dashboard
   - Or navigate to `/quiz/`

2. **Select Topic & Difficulty**
   - Choose from 9 topic cards
   - Select Basic, Intermediate, or Advanced level
   - Previous scores shown as badges

3. **Take Quiz**
   - Questions displayed one at a time
   - Click "Show Answer" to reveal correct answer
   - Navigate using Previous/Next buttons
   - Progress dots show current position
   - Timer tracks time spent

4. **Submit & View Results**
   - Click "Submit Quiz" on last question
   - View score, percentage, and time
   - Review all questions with answers
   - Retake quiz or return to hub

5. **Track Progress**
   - View previous attempts on quiz detail page
   - See performance history
   - Compare scores across attempts

### For Admins

1. **Manage Quizzes**
   - Access Django admin at `/admin/`
   - Create/edit quizzes and questions
   - Activate/deactivate quizzes
   - Set question order

2. **View Metrics**
   - Navigate to `/manage/students/`
   - See quiz statistics dashboard
   - View top performers
   - Monitor recent attempts

3. **Student Details**
   - Click on any student
   - View their quiz attempts
   - See average scores
   - Review performance history

## Setup Instructions

### 1. Install Django
```bash
pip install django
```

### 2. Apply Migrations
```bash
python manage.py migrate
```

### 3. Populate Quiz Data
```bash
python setup_quizzes.py
```

This creates:
- 27 quizzes (9 topics × 3 difficulty levels)
- 135 questions (5 per quiz)

### 4. Create Admin User (if needed)
```bash
python manage.py createsuperuser
```

### 5. Run Server
```bash
python manage.py runserver
```

## URLs

- **Quiz Hub**: `/quiz/`
- **Quiz Detail**: `/quiz/<quiz_id>/`
- **Submit Quiz**: `/quiz/attempt/<attempt_id>/submit/`
- **Results**: `/quiz/attempt/<attempt_id>/results/`
- **Admin Students**: `/manage/students/`
- **Django Admin**: `/admin/`

## Customization

### Adding New Topics
Edit `courses/models.py`:
```python
TOPIC_CHOICES = [
    ('LINUX', 'Linux'),
    ('YOUR_TOPIC', 'Your Topic Name'),  # Add here
    ...
]
```

### Adding Questions
Use Django admin or create script similar to `setup_quizzes.py`

### Styling
All templates use Bootstrap 5 dark theme with custom CSS

## Technical Details

### Frontend
- Bootstrap 5 dark theme
- Custom CSS animations
- Vanilla JavaScript for interactions
- Progress tracking with dots
- Timer functionality

### Backend
- Django views with authentication
- AJAX for quiz submission
- JSON responses
- Query optimization with select_related()

### Security
- CSRF protection
- Login required decorators
- User-specific data filtering
- Staff-only admin views

## Future Enhancements

Potential improvements:
- [ ] Multiple choice questions
- [ ] Timed quizzes
- [ ] Leaderboards
- [ ] Quiz categories/tags
- [ ] Question explanations
- [ ] Difficulty recommendations
- [ ] Achievement badges
- [ ] Export results to PDF
- [ ] Quiz sharing
- [ ] Randomized question order

## Support

For issues or questions:
1. Check Django logs
2. Verify migrations are applied
3. Ensure quiz data is populated
4. Check user permissions
5. Review browser console for JS errors
