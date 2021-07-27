from django.contrib import admin
from .models import Question

@admin.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question_text',
        'create_at',
        'updated_at',

    )

# Register your models here.
