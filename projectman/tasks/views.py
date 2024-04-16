from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .mixins import WeekMixin
from .forms import CommentForm, ProjectForm , TaskForm, PerformanceMetricForm, TaskProgressUpdateForm
from .models import Announcement,Project, Task, User, Comment, PerformanceMetric,TaskStatus
from django.views.generic import UpdateView, DeleteView, View
from django.shortcuts import render,redirect,get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import mimetypes
from django.utils import timezone
from users.models import UserSession

from django.contrib.sessions.models import Session

# Create your views here.

def base_temp(request):
    week_mixin = WeekMixin()
    week_start = week_mixin.get_week_start_date()
    week_end = week_mixin.get_week_end_date()
    context = {
        'week_start':week_start,
        'week_end':week_end,
    }
    return render(request, 'tasks/base.html', context)


def user_performance_view(request,team_id, user_id):
    user = User.objects.get(pk=user_id)
    performance_metrics = PerformanceMetric.objects.filter(user_id=user_id)        
    context = {
        'user': user,
        'performance_metrics': performance_metrics
    }
    return render(request, 'tasks/user_detail.html', context)


@login_required(login_url="login")
def home(request):
    user = request.user
    ongoing_tasks = Task.objects.filter(assigned_to=user,status__in=[TaskStatus.OPEN, TaskStatus.IN_PROGRESS])
    announcement = Announcement.objects.all()[:5]
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_ids = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id = data.get('_auth_user_id', None)
        if user_id:
            user_ids.append(user_id)
    active_users_ = User.objects.filter(id__in=user_ids)
    context = {'active_users':active_users_,'announcement':announcement, 'ongoing_tasks':ongoing_tasks}
    return render(request, 'tasks/home.html',context)

def AboutView(request):
    return render(request, 'tasks/about.html')



#detailviews

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project=project)
    total_tasks = project.task_set.count()
    completed_tasks = project.task_set.filter(status='done').count()
    print("Completed :", completed_tasks, " -- Total: ", total_tasks)
    if total_tasks != 0:
        progress_percentage = (completed_tasks / total_tasks) * 100
        progress = f"{progress_percentage}%"
    else:
        progress_percentage = 0
        progress = f"{progress_percentage}%"
    return render(request, 'tasks/project_detail.html', {'project': project, 'progress_percentage': progress,'tasks': tasks,})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    print("Task: ", task)
    comments = Comment.objects.filter(task=task).order_by('-timestamp')[:5]
    progress_percentage = 100 if task.status == 'done' else task.progress
    return render(request, 'tasks/task_detail.html', {'task': task, 'progress_percentage': progress_percentage, 'comments': comments})


# CreateViews
##

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user 
            form.save()
            messages.success(request, 'Project created successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm()

    return render(request, 'tasks/project_add.html', {'form': form})

@login_required
def create_comment(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('task_detail', task_id=task.id)
    else:
        form = CommentForm()

    return render(request, 'tasks/comment_add.html', {'form': form, 'task': task})

@login_required
def create_task(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('project_detail', project_id=project.id)
    else:
        form = TaskForm()
        
    return render(request, 'tasks/task_add.html', {'form': form, 'project': project})


# ListViews
##

def project_list(request):
    projects = Project.objects.all().order_by('-end_date')
    return render(request, 'tasks/project_list.html', {'projects': projects})

@login_required
def user_task_list(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    context = {
        'tasks': tasks,
    }
    return render(request, 'tasks/user_task_list.html', context)

def completed_projects_view(request):
    completed_projects = Project.objects.filter(status='COMPLETED')
    context = {
        'completed_projects': completed_projects
    }
    return render(request, 'tasks/completed_projects.html', context)


# UpdateViews
##
class ProjectUpdate(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'tasks/project_update.html'
    context_object_name = 'project'
    success_url = reverse_lazy('project_list')
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    context_object_name = 'task'
    
    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'task_id': self.object.pk})
    
@login_required
def update_progress_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, assigned_to=request.user)

    if request.method == 'POST':
        form = TaskProgressUpdateForm(request.POST, instance=task)
        if form.is_valid():
            updated_task = form.save()
            updated_task.calculate_progress_percentage()
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskProgressUpdateForm(instance=task)

    return render(request, 'tasks/task_progress_update.html', {'form': form, 'task': task})


#DeleteViews
##

class ProjectDelete(DeleteView):
    model = Project
    template_name = 'tasks/project_delete.html'
    success_url = reverse_lazy('project_list')
    

class ProfileDelete(DeleteView):
    model = User
    template_name = 'tasks/profile.html'
    success_url = reverse_lazy('profile')
    
class TaskDelete(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        return render(request, 'tasks/task_delete.html', {'task': task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return redirect('project_list')

    
def open_project_document(request, project_id):
    document = get_object_or_404(Project, pk=project_id)
    with open(document.project_file.path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')  
        response['Content-Disposition'] = f'inline; filename="{document.project_file.name}"'
        return response


##recording the performance of the team member
def record_performance(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    timeliness = request.POST.get('timeliness')
    quality_of_work = request.POST.get('quality_of_work')
    
    # Create or update performance metric for the task and user
    PerformanceMetric.objects.update_or_create(
        user=request.user,
        task=task,
        defaults={
            'timeliness': timeliness,
            'quality_of_work': quality_of_work
        }
    )
    
    
def performance_metric_form(request):
    if request.method == 'POST':
        form = PerformanceMetricForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or another view
            return redirect('home')
    else:
        form = PerformanceMetricForm()
    return render(request, 'tasks/performance_metric.html', {'form': form})    