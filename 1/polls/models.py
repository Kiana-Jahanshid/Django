import datetime
from datetime import timezone
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField("Date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self): 
        # if that question is published recently or not 
        # it will return false or true
        # if the difference is more than 1 day or not 
        # if it's more than 1 day --> return false 
        # if it's less than 1 day --> it has published recently , and it's true
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1) 

class Choice(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE) # this will define relation between Question & Choice classes
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text