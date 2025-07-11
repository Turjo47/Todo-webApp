from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
# Create your views here.

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tasks/tasks_list.html', {'tasks':tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority', 'medium')
        Task.objects.create(
            user= request.user,
            title = title,
            description = description,
            priority = priority,
        )
        return redirect('task_list')
    return render(request, 'tasks/tasks_form.html')

@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.priority = request.POST.get('priority', 'medium')
        task.is_completed = 'is_completed' in request.POST
        task.status = request.POST.get('status', task.status)
        task.save()
        return redirect('task_list')
    return render (request, 'tasks/task_form.html', {'tasks':task})

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')