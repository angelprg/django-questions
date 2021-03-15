"""Test File for question models"""
from django.test import TestCase
from django.core.validators import ValidationError
from django.contrib.auth import get_user_model

from questions.models import Question, QuestionCategory


def test_user(email='testuser@gmail.com', password="SecurePassword"):
    """Creating temporal user for testing"""
    return get_user_model().objects.create_user(email, password)


def test_category(name='Test Category', description="Category for testing"):
    """Creating temporal category for testing"""
    return QuestionCategory.objects.create(name=name, description=description)


class ModelTests(TestCase):

    def test_create_questions_category(self):
        """Testing creating new category successful"""
        name = "Example Category"
        description = "Category for testing purposes"
        category = QuestionCategory.objects.create(
            name=name,
            description=description
            )
        self.assertEqual(category.name, name)
        self.assertEqual(category.description, description)

    def test_create_unamed_questions_category_fail(self):
        """Testing fail on creating new category without a name"""
        description = "Category for testing purposes"
        category = QuestionCategory.objects.create(description=description)
        with self.assertRaises(ValidationError):
            category.full_clean()

    def test_create_question(self):
        """Testing create a new question"""
        newQuestion = Question.objects.create(
            question="Could this question pass the test?",
            category=test_category(),
            author=test_user()
        )

        self.assertEqual(
            newQuestion.question,
            "Could this question pass the test?"
            )
