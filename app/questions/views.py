from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages

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


@login_required(redirect_field_name='questions')
def question_add(request):
    if request.method == 'POST':
        question = request.POST['question']
        category_id = request.POST['category']
        user_id = request.user.id

        question = Question(
            question=question,
            category_id=category_id,
            author_id=user_id,
        )
        question.save()
        
        messages.success(request, "Su pregunta se generó correctamente")
        return redirect('questions')

    categories = QuestionCategory.objects.all()
    context = {'categories': categories}
    return render(request, 'questions/add.html', context)


@login_required(redirect_field_name='questions')
def question_respond(request, question_id):

    question = Question.objects.get(id=question_id)
    if question is None:
        messages.error(request, "Error al procesar su solicitud. Intente nuevamente")
        return redirect('questions')

    if request.method == 'POST':
        response = request.POST['response']
        if question:
            question.response = response
            question.responder_id = request.user.id
            question.save()
            messages.success(request, "Su pregunta se generó correctamente")
            return redirect('questions')

    context = {'question': question}
    return render(request, 'questions/respond.html', context)
