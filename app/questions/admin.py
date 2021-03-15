from django.contrib import admin

from questions.models import Question, QuestionCategory


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )


admin.site.register(QuestionCategory)
