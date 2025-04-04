from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def task_list(request):
    tasks = None
    return render (request, "tasks/task_list.html", {"task":tasks})