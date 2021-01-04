from django.shortcuts import render
from django.views import generic
from task.models import Task, Num
from task.forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

def home(request):

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    number = Num(number=num_visits)
    number.save()
    context = {'num_visits': number
    }

    return render(request, 'task/home.html',context)
@login_required
def taskview(request):
    task = Task.objects.all()
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
    else:
        form = TaskForm()
    context={
        'task':task,
        'form':form,
    }
    return render(request, 'task/list_task1.html',context)
#be.az
class TaskDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Task
    template_name = 'task/task_detail.html'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False
