from django.urls import path
from task import views as task_views
# Mapping to view functions

urlpatterns = [
    path('', task_views.home, name='home-task'),
]


