from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo

def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'todo/index.html', { "todo_items": todo_items })

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    if (content != ''):
        created_obj = Todo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect(reverse('todo:home'))

@csrf_exempt
def delete_todo(request, todo_id):
    delete_item = Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect(reverse('todo:home'))