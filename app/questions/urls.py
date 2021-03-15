from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.questions, name='questions'),
    path('reportes', views.reports, name='reports'),
]