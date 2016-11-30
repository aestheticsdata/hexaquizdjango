from django.contrib import admin

from .models import *


class QuizQuestionsInline(admin.TabularInline):
    model = QuizQuestion
    extra = 0


class AnwsersInline(admin.TabularInline):
    model = Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnwsersInline, QuizQuestionsInline]
    list_filter = ['quiz']


admin.site.register(User)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz)
admin.site.register(Score)
admin.site.register(UserAnswer)

admin.site.site_header = 'Hexaquiz admin'
admin.site.site_title = 'Hexaquiz admin'
