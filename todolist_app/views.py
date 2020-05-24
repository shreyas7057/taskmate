from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid:
            form.save(commit=False).manager=request.user
            form.save()
        messages.success(request,"New Task Added")
        return redirect('todolist')
    else:
        all_task =TaskList.objects.filter(manager=request.user)
        paginator = Paginator(all_task,3)
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)
        context = {
            'all_task':all_task,
        }
        return render(request,"todolist.html",context)

@login_required
def edit_task(request,task_id):
    if request.method == "POST":
        task_obj = TaskList.objects.get(pk=task_id) 
        form = TaskForm(request.POST or None,instance=task_obj)
        if form.is_valid:
            form.save()

        messages.success(request,"Task Edited")
        return redirect('todolist')
    else:
        task_obj =TaskList.objects.get(pk=task_id)
        context = {
            'task_obj':task_obj,
        }
        return render(request,"edit.html",context)


@login_required
def complete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        task.done= True
        task.save()
    else:
        messages.error("Access Denied","You are not allowed")
    return redirect('todolist')


@login_required
def pending_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done= False
    task.save()
    return redirect('todolist')

@login_required
def delete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        task.delete()
    else:
        messages.error("Access Denied","You are not allowed")
    return redirect('todolist')


@login_required
def contact(request):
    context = {
        'contactext':"This is text from contact Page",
    }
    return render(request,"contactus.html",context)


def about(request):
    context = {
        'abouttext':"This is text from about us Page",
    }
    return render(request,"aboutus.html",context)


def index(request):
    context = {
        'indextext':"This is text from index Page",
    }
    return render(request,"index.html",context)