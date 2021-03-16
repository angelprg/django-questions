from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.questions, name='questions'),
    path('question/add', views.question_add, name='question_add'),
    path('question/respond/<str:question_id>/' , views.question_respond, name='question_respond'),
    path('reportes', views.reports, name='reports'),
]