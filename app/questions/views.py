from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator  # EmptyPage, PageNotAnInteger,
from django.contrib import messages
from django.db.models import Count, Q

from questions.models import Question, QuestionCategory


def questions(request):
    context = {}
    questions = Question.objects.order_by('-created_at')
    paginator = Paginator(questions, 25)
    page = request.GET.get('page')
    paged_questions = paginator.get_page(page)
    context = {'qs': paged_questions}
    return render(request, 'questions/index.html', context)


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
        messages.error(
            request,
            "Error al procesar su solicitud. Intente nuevamente"
        )
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


def reports(request):
    qs = Question.objects.all()

    # Responded Filters
    is_responded = Count('pk', filter=Q(responded_at__isnull=False))
    is_not_responded = Count('pk', filter=Q(responded_at__isnull=True))

    # Queries
    questions_by_category = qs.values('category__name').annotate(
        is_responded=is_responded
        ).annotate(is_not_responded=is_not_responded)
    questions_by_created = qs.values('created_at__date').annotate(
        is_responded=is_responded
        ).annotate(is_not_responded=is_not_responded).order_by('-created_at__date')

    questions_responded = qs.filter(responder_id__isnull=False).count()
    questions_not_responded = qs.filter(responder_id__isnull=True).count()

    context = {
        'questions_by_category': questions_by_category,
        'questions_by_created': questions_by_created,
        'questions_responded': questions_responded,
        'questions_not_responded': questions_not_responded,
    }
    return render(request, 'reports/index.html', context)
