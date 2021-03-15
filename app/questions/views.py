from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from questions.models import Question, QuestionCategory

def questions(request):
    context = {}
    questions = Question.objects.order_by('-created_at')
    paginator = Paginator(questions, 25)
    page = request.GET.get('page')
    paged_questions = paginator.get_page(page)
    context = {'qs': paged_questions}
    return render(request, 'questions/index.html', context)


def reports(request):
    context = {}
    return render(request, 'reports/index.html', context)
