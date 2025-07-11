from django.shortcuts import render, redirect
from django.http import HttpResponse

todo_items=[]
# Create your views here.
def todo_view(request):
    return render(request, "tasks/task_list.html")