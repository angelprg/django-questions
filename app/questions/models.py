"""Question models"""
from django.conf import settings
from django.db import models


class QuestionCategory(models.Model):
    """Question Category Model"""
    name = models.CharField(
        "Category Name",
        max_length=50,
        blank=False,
        null=False
        )
    description = models.TextField(
        "Category Description",
        max_length=250,
        blank=True,
        null=True
        )


class Question(models.Model):
    """Question model"""
    name = models.CharField(
        "Question",
        max_length=500,
        blank=False,
        null=False
        )
    category = models.ForeignKey("QuestionCategory", on_delete=models.PROTECT)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=False,
        null=False
        )
    response = models.TextField(
        "Question Response",
        max_length=1000,
        blank=True,
        null=True
        )
    responder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="responses"
        )

    created_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(blank=True, null=True)
