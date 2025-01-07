import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.test import Client

class QuestionModelTest(TestCase):

    #------------- TESTING MODEL(DB) part ----------------

    def test_was_published_recently_with_future_question(self): # distant future != recently --> must return False
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(publish_date=time)
        self.assertIs(future_question.was_published_recently() , False)

    def test_was_published_recently_with_old_question(self): # distant past != recently --> must return False
        time = timezone.now() - datetime.timedelta(days=1 , seconds=1)
        old_question = Question(publish_date= time)
        self.assertIs(old_question.was_published_recently() , False)

    def test_was_published_recently_with_recent_question(self):
        #was_published_recently() returns True for questions whose pub_date is within the last day.
        # It will return True if any posts have been published in the recent 23 hours.
        time = timezone.now() - datetime.timedelta(hours=23)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


    # -------------- TESTING view part ----------------:
    # we create an agent named client , it means we create a code wich is palying a role as a user 
    # it is kind of " User behavior simulation "
    















# for running this file :
'''
python manage.py test polls
'''
