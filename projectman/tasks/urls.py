from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProfileDelete, ProjectDelete, TaskDelete
from .views import ProjectUpdate, TaskUpdate
from .views import create_project, create_comment,create_task

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
    
    path('task_view/<int:task_id>/delete/',TaskDelete.as_view(), name='task_delete'),
    path('project_view/<int:pk>/delete/',ProjectDelete.as_view(), name='project_delete'),
    path('profile_view/<int:pk>/delete/',ProfileDelete.as_view(), name='profile_delete'),
    
    
    #updateviews
    ##
    
    path('task_view/<int:pk>/',TaskUpdate.as_view(), name='task_update'),
    path('project_view/<int:pk>/',ProjectUpdate.as_view(), name='project_update'),
    path('tasks/<int:task_id>/progress_update/', views.update_progress_task, name='update_task_progress'),
    
    
    #listviews
    ##
    path('projects/', views.project_list, name='project_list'),
    path('tasks/list/', views.user_task_list, name='user_task_list'),
    path('completed-projects/', views.completed_projects_view, name='completed_projects'),
    
    
    ##detailviews
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/download/', views.open_project_document, name='projfile_download'),
    path('members/<int:team_id>/<int:user_id>/', views.user_performance_view, name='member_detail'),
    
    ##Performance metrics
    path('performance_metrics/',views.performance_metric_form, name="performance_metric_form"),
     
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)