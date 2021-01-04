from django.forms import ModelForm
from task.models import Task

# create form fields

class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields =['tasktitle', 'taskdetail']



