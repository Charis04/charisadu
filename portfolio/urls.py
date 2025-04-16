from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dev', views.dev_home, name='dev-home'),
    path('project/<int:id>', views.project, name='project'),
]
