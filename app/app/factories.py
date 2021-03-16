
import unidecode
import factory
import factory.django
from factory.faker import faker
from django.contrib.auth import get_user_model

from questions.models import Question, QuestionCategory

FAKE = faker.Faker('es_MX')


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'users.User'
        django_get_or_create = ('email',)

    first_name = factory.LazyAttribute(lambda _: FAKE.first_name())
    last_name = factory.LazyAttribute(lambda _: FAKE.last_name())
    email = factory.LazyAttribute(
        lambda a: '{}.{}@example.com'.format(
            unidecode.unidecode(a.first_name).replace(' ',''),
            unidecode.unidecode(a.last_name).replace(' ',''),
            ).lower()
        )
    # password = FAKE.password()
    password = factory.PostGenerationMethodCall('set_password', 'SuperPassword123')
    


class QuestionWithResponseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    question = factory.LazyAttribute(
        lambda _: f"¿{FAKE.sentence(nb_words=30)[:100]}?"
    )
    category = factory.Iterator(QuestionCategory.objects.all())
    author = factory.Iterator(get_user_model().objects.all())
    response = factory.LazyAttribute(
        lambda _: FAKE.sentence(nb_words=30)[:200]
    )
    responder = factory.Iterator(get_user_model().objects.all())


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    question = factory.LazyAttribute(
        lambda _: f"¿{FAKE.sentence(nb_words=30)[:100]}?"
    )
    category = factory.Iterator(QuestionCategory.objects.all())
    author = factory.Iterator(get_user_model().objects.all())
