from django.contrib import admin
from .models import Question, Choice
# Register your models here.


# admin.site.register(Question)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Text', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)  # 创建一个模型后台类，接着将其作为第二个参数传给 admin.site.register()


# class ChoiceAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Choice Text', {'fields': ['choice_text']}),
#         ('Votes', {'fields': ['votes']}),
#     ]


# admin.site.register(Choice)
