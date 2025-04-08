from django.shortcuts import render, redirect
from django.http import HttpResponse

todo_items=[]
# Create your views here.
def todo_view(request):
    global todo_items

    if request.method == 'POST':
        task = request.POST.get('task')
        if task:
            todo_items.append(task)
        
        return redirect ('todo')
    return render(request, 'task/todo.html',{'task':todo_items})