from django.contrib.auth import get_user_model
from django.utils import timezone
from factory.faker import faker

from questions.models import Question, QuestionCategory
from app.factories import UserFactory, QuestionFactory, \
    QuestionWithResponseFactory

FAKE = faker.Faker('es_MX')

# Set defined categories and get existing ones.
defined_categories = ["Técnica", "Legal", "Administrativa", "Económicas"]
existing_categories = [
    category.name for category in QuestionCategory.objects.all()
]


def populate():

    # Create defined categories
    for category in defined_categories:
        if category not in existing_categories:
            QuestionCategory.objects.create(name=category)

    # Create 500 users
    current_users = len(get_user_model().objects.all())
    rest_users = 500 - current_users if current_users < 500 else 0
    print(f'Creating {rest_users} users')
    UserFactory.create_batch(rest_users)

    # Create 1000 (or complementary to 1000) questions with response
    current_questions = len(Question.objects.filter(responder__isnull=False))
    rest_questions = 1000 - current_questions \
        if current_questions < 1000 else 0
    print(f'Creating {rest_questions} questions with response')
    QuestionWithResponseFactory.create_batch(rest_questions)

    # Create 300 (or complementary to 300) questions without response
    current_questions = len(Question.objects.filter(responder__isnull=True))
    rest_questions = 300 - current_questions if current_questions < 300 else 0
    print(f'Creating {rest_questions} questions without response')
    QuestionFactory.create_batch(rest_questions)

    print('Updating questions with fake dates')
    for question in Question.objects.all():
        # Updating questions with random dates
        question.created_at = FAKE.past_datetime(
            start_date='-120d',
            tzinfo=timezone.get_current_timezone()
        )
        if question.responder is not None:
            question.responded_at = FAKE.date_time_between(
                start_date=question.created_at,
                end_date='now',
                tzinfo=timezone.get_current_timezone()
            )
        else:
            question.responded_at = None
        question.save()
