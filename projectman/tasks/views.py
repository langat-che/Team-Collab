from django.contrib.auth.decorators import login_required
from .mixins import WeekMixin
from .forms import CommentForm, ProjectForm , TaskForm
from .models import Announcement,Project, Task, Travel, User, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect,get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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

def home(request):
    announcement = Announcement.objects.all()[:5]
    return render(request, 'tasks/home.html',{'announcement':announcement})

def AboutView(request):
    return render(request, 'tasks/about.html')



#detailviews

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project=project)
    latest_comments = Comment.objects.filter(task__project=project).order_by('-timestamp')[:5]
    return render(request, 'tasks/project_detail.html', {'project': project, 'tasks': tasks, 'latest_comments': latest_comments})

    

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = Comment.objects.filter(task=task).order_by('-timestamp')[:5]
    return render(request, 'tasks/task_detail.html', {'task': task, 'comments': comments})

# CreateViews
##

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
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
    projects = Project.objects.all()
    return render(request, 'tasks/project_list.html', {'projects': projects})





    
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
    template_name = 'tasks/task_view.html'
    context_object_name = 'task'
    
    

#DeleteViews
##

class ProjectDelete(DeleteView):
    model = Project
    template_name = 'tasks/project_delete.html'
    success_url = reverse_lazy('project_view')
    

class ProfileDelete(DeleteView):
    model = User
    template_name = 'tasks/profile.html'
    success_url = reverse_lazy('profile')

    
class TaskDelete(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task_view')