import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.test import Client
from django.urls import reverse


#------------- TESTING MODEL(DB) part ----------------
class QuestionModelTest(TestCase):

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

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"],[question])

    def test_future_question(self):
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"],[question])

    def test_two_past_questions(self):
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"],[question2, question1])



class QuestionDetailViewTests(TestCase):
    
    def test_future_question(self):
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)








# for running this file :
'''
python manage.py test polls
'''
