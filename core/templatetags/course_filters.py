from django import template

register = template.Library()

@register.filter
def filter_by_course(enrollments, course):
    """Check if user is enrolled in a specific course"""
    return enrollments.filter(course=course).exists()

@register.filter
def get_item(dictionary, key):
    """Get item from dictionary by key"""
    if dictionary is None:
        return None
    return dictionary.get(str(key))
