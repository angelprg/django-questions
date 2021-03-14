"""Test File for question models"""
from django.test import TestCase
from django.core.validators import ValidationError

from questions.models import QuestionCategory


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

    # def test_create_question(self):
    #     """Testing create a new question"""
    #     question = "Could this question pass the test?"
    #     author = 
