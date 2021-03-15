"""Question models"""
from django.conf import settings
from django.db import models
from django.utils import timezone


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

    def __str__(self):
        return f"{self.name}"


class Question(models.Model):
    """Question model"""
    question = models.CharField(
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

    def __init__(self, *args, **kwargs):
        super(Question, self).__init__(*args, **kwargs)
        self._responder = self.responder

    def save(self, *args, **kwargs):
        if not self._responder and self.responder:
            self.responded_at = timezone.now()
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return f"({self.id}) {self.question[:15]}"
