from django.urls import path
from .views import TodoList, TodoDetail, TodoAdd, TodoDelete, TodoEdit, mark_as_done



urlpatterns = [
     ##todoapp
    path('todo/', TodoList.as_view(), name="todolist"),
    path('todo/<int:pk>/', TodoDetail.as_view(), name="tododetail"),  
    path('add/', TodoAdd.as_view(), name="todoadd"),
    path('todo/edit/<int:pk>/', TodoEdit.as_view(), name="todoedit"),
    path('todo/delete/<int:pk>/', TodoDelete.as_view(), name="tododelete"),
    path('todo/<int:todo_id>/mark_as_done/', mark_as_done, name='mark_as_done'),
]
