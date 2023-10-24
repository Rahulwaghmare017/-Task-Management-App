from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, TaskStatusForm, TaskUpdateForm

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_manager/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_manager/task_detail.html', {'task': task})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_manager:task_list')
    else:
        form = TaskForm()
    return render(request, 'task_manager/task_form.html', {'form': form})

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_manager:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_manager/task_form.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_manager:task_list')
    return render(request, 'task_manager/task_confirm_delete.html', {'task': task})
def change_task_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        form = TaskStatusForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_manager:task_list')  # Redirect to the task list after status change

    else:
        form = TaskStatusForm(instance=task)

    return render(request, 'task_manager/change_task_status.html', {'form': form, 'task': task})

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_manager:task_list')  # Redirect to the task list after updating the task
    else:
        form = TaskUpdateForm(instance=task)

    return render(request, 'task_manager/update_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_manager:task_list')  # Redirect to the task list after deleting the task

    return render(request, 'task_manager/delete_task.html', {'task': task})