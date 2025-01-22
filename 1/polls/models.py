import datetime
from django.utils import timezone
from django.db import models
from khayyam import JalaliDatetime

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
        #print(self.publish_date)
        return timezone.now() - datetime.timedelta(days=1) <= self.publish_date <= timezone.now()
    
    def jalali_datetime(self):
        # example of publish date value : 2025-01-05 10:06:31+00:00
        datetime_obj = datetime.datetime.fromisoformat(str(self.publish_date))
        jalali_datetime = JalaliDatetime(datetime_obj)
        jalali = jalali_datetime.strftime('%Y-%m-%d %H:%M:%S')
        print(f"Jalali Date: {jalali}")
        return jalali

class Choice(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE) # this will define relation between Question & Choice classes
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    

