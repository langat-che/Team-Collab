from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import TodoForm
# Create your views here.


##todo list
class TodoList(ListView):
    model = Todo
    context_object_name = "todo"
    ordering = ("-created")
    template_name = 'todo_app/todo_list.html'
    

##Todo detail view
class TodoDetail(DetailView):
    model = Todo
    context_object_name="todo"
    template_name="todo_app/todo_detail.html"
    
##Add todo
class TodoAdd(CreateView):
    model = Todo
    # fields = ('__all__')
    form_class = TodoForm
    template_name = 'todo_app/todo_add.html'
    success_url = reverse_lazy("todolist")
    
## Update view    
class TodoEdit(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo_app/todo_edit.html'
    success_url = reverse_lazy('todolist')
    
    
## Delete view
class TodoDelete(DeleteView):
    model = Todo
    template_name = 'todo_app/todo_delete.html'
    success_url = reverse_lazy('todolist')
    
