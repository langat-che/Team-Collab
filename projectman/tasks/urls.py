from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProfileDelete, ProjectDelete, TaskDelete
from .views import ProjectUpdate, TaskUpdate
from .views import project_list, project_detail, task_detail, create_project, create_comment,create_task, assigned_tasks


urlpatterns = [
    path('',views.home,name='home'),
    path('about/', views.AboutView, name='about'),
    
    #createviews
    ##
    path('projects/<int:project_id>/create_task/', create_task, name='task_add'),
    path('create_project/', create_project, name='project_add'),
   
    path('tasks/<int:task_id>/create_comment/', create_comment, name='comment_add'),
    
    #deleteviews
    ##
    
    path('task_view/<int:pk>/delete/',TaskDelete.as_view(), name='task_delete'),
    path('project_view/<int:pk>/delete/',ProjectDelete.as_view(), name='project_delete'),
    path('profile_view/<int:pk>/delete/',ProfileDelete.as_view(), name='profile_delete'),
    
    
    #updateviews
    ##
    
    path('task_view/<int:pk>/',TaskUpdate.as_view(), name='task_update'),
    path('project_view/<int:pk>/',ProjectUpdate.as_view(), name='project_update'),
    
    
    #listviews
    ##
    path('projects/', project_list, name='project_list'),
    
    
    ##detailviews
    path('assigned_tasks/', assigned_tasks, name='assigned_tasks'),
    path('tasks/<int:task_id>/', task_detail, name='task_detail'),
    path('projects/<int:project_id>/', project_detail, name='project_detail'),
     
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)