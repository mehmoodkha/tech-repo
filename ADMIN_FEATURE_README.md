# Admin Student Management Feature

## Overview
Admin users can now view and manage all student dashboards, including updating their RHCSA/RHCE topic progress.

## Features Added

### 1. Student Progress Model
- New `StudentProgress` model in `courses/models.py`
- Stores RHCSA/RHCE topic completion data in JSON format
- Tracks last update time
- Methods to calculate completion percentage and count

### 2. Admin Views
- **Student List** (`/admin/students/`): View all students with their progress
- **Student Dashboard** (`/admin/students/<id>/`): View and edit individual student progress
- **Update Progress API** (`/admin/students/<id>/update-progress/`): Save progress changes

### 3. Templates
- `admin_students.html`: Lists all students with enrollment and progress info
- `admin_student_dashboard.html`: Full student dashboard with editable checklist
- Updated `dashboard.html`: Syncs with database for student progress
- Updated `base.html`: Added "Manage Students" button for admin users

### 4. Access Control
- Only staff users (admins) can access student management pages
- Uses `@staff_member_required` decorator for protection

## How to Use

### For Admin Users:

1. **Login as admin** (must have `is_staff=True`)

2. **Access Student Management**:
   - Click "Manage Students" button in the navbar
   - Or navigate to: `/admin/students/`

3. **View Student List**:
   - See all students with their enrollment count and RHCSA progress
   - Progress bars show completion percentage

4. **Edit Student Progress**:
   - Click "View Dashboard" for any student
   - Check/uncheck RHCSA topics
   - Click "Save Changes" to update the database
   - Progress bar updates in real-time

### For Students:

1. **View Your Dashboard**:
   - Navigate to `/dashboard/`
   - Your progress loads from the database
   - Check/uncheck topics (saved to localStorage and synced)

## Database Changes

New migration created: `courses/migrations/0002_studentprogress.py`

## URLs Added

```python
path('admin/students/', core_views.admin_students, name='admin_students'),
path('admin/students/<int:user_id>/', core_views.admin_student_dashboard, name='admin_student_dashboard'),
path('admin/students/<int:user_id>/update-progress/', core_views.admin_update_progress, name='admin_update_progress'),
```

## Testing

To test the feature:

1. Run the development server:
   ```bash
   python manage.py runserver
   ```

2. Create a superuser (if not already):
   ```bash
   python manage.py createsuperuser
   ```

3. Create test students through registration or Django admin

4. Login as admin and navigate to `/admin/students/`

5. Select a student and update their progress

## Notes

- Progress is stored in JSON format for flexibility
- Real-time UI updates without page refresh
- CSRF protection on all POST requests
- Admin changes are immediately reflected in student's dashboard
