from django.contrib import admin
from .models import Question ,Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None , 
                {"fields":["question_text"]}) ,
                ("Date_information", {"fields":["publish_date"] , "classes":["collapse"]}) ] # Date_information is a title of date field
    inlines = [ChoiceInline]
    list_display =["question_text" , "publish_date" , "was_published_recently"]
    list_filter = ["publish_date"]
    search_fields =["question_text"]

admin.site.register(Question , QuestionAdmin)
admin.site.register(Choice) # we can access to choice directly , and we can add choices independently 