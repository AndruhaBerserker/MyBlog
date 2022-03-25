from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def saved_task(request):
    tasks = Task.objects.all()
    return render(request, 'main/saved_task.html', {'title': 'Saved', 'tasks': tasks})


def index(requests):
    return render(requests, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saved_task')
        else:
            error = 'Форма неверна'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_task.html', context)

