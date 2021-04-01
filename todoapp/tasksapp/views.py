from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    tasks = Task.objects.all()
    form = TasksForm()

    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'tasks.html', {'tasks': tasks, 'form': form})


def complete(request):
    tasks = Task.objects.filter(completed=True)
    form = TasksForm()

    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'tasks.html', {'tasks': tasks, 'form': form})


def incomplete(request):
    tasks = Task.objects.filter(completed=False)
    form = TasksForm()

    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'tasks.html', {'tasks': tasks, 'form': form})


def update(request, id):
    task = Task.objects.get(id=id)
    form = TasksForm(instance=task)

    if request.method == "POST":
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'update.html', {'form':form})


def delete(request, id):
    task = Task.objects.get(id=id)

    if request.method == "POST":
        task.delete()
        return redirect('/')

    return render(request, 'delete.html', {'task': task})