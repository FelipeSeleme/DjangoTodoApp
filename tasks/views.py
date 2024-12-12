from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Página inicial
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')  # Redireciona para a página principal

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)


# Atualizar tarefa
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Salva a tarefa atualizada
        return redirect('/')  # Redireciona para a página principal

    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)


# Excluir tarefa
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)  # Pega a tarefa a ser excluída

    if request.method == 'POST':
        item.delete()  # Exclui a tarefa
        return redirect('/')  # Redireciona para a página inicial

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)
