from django.contrib import admin
from polls.models import Question,Choice
class ChoiceInline(admin.TabularInline):
     model=Choice
     extra=2

class QuestionAdmin(admin.ModelAdmin):
   
   list_display=('question_text','pub_date','was_published_recently')
   list_filter=['pub_date']
   search_field=['question_text']
   fieldsets=[
     (None,   {'fields': ['question_text']}),
     ('Date', {'fields' : ['pub_date'],'classes': ['collapse']}),
   ]

   inlines=[ChoiceInline]

admin.site.register(Question,QuestionAdmin)

