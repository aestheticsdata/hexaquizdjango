from django.contrib import admin

from .models import *


class QuizQuestionsInline(admin.TabularInline):
    model = QuizQuestion
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = (QuizQuestionsInline,)


class QuizAdmin(admin.ModelAdmin):
    inlines = (QuizQuestionsInline,)


admin.site.register(User)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Score)
admin.site.register(Answer)
admin.site.register(UserAnswer)

admin.site.site_header = 'Hexaquiz admin'
admin.site.site_title = 'Hexaquiz admin'
