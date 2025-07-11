from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PRIORITY_CHOICES = [
    ('low','Low'),
    ('med', 'Medium'),
    ('high', 'High'),
]

STATUS_CHOICES= [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
]
class Task(models.Model):
    user = models.ForeignKey(on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='med')
    