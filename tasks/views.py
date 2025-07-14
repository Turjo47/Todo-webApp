from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from .models import Task
# Create your views here.

class TaskList(ListView):
    model = Task
    


