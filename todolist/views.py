from django.shortcuts import redirect, render
from .models import *
# Create your views here.
nom = Todo.objects.all()
def home(request):
    return render(request, 'home.html')
def todos(request):
    if request.method == 'POST':
        Todo.objects.create(
            nom = request.POST.get('nom'),
            batafsil = request.POST.get('batafsil'),
            status = request.POST.get('status'),
            vaqt = request.POST.get('vaqt'),
        )
        return redirect('todo')
    return render(request, 'todo.html',{'nom':nom})

def todor(request, son):
    a = Todo.objects.get(id=son)
    a.delete()
    return redirect('todo')