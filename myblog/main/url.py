from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('task', views.create_task, name='create_task'),
    path('saved', views.saved_task, name='saved_task')
]
