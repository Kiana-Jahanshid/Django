from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from django.http import Http404
from django.template import loader # for loading html files
from django.urls import reverse 
from django.db.models import F
from django.utils import timezone
from django.views import generic
from .models import Question , Choice

# Create your views here.
# Numbers of pages in our website == Numbers of functions in this file
# for calling these functions , we should define route in polls/urls.py

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self): # this will return last 5 question
        return Question.objects.order_by("-publish_date")[:5]

class DetailView(generic.DetailView):
    model = Question 
    template_name = "polls/detail.html"
    #def get_queryset(self):
    #   return Question.objects.filter(publish_date=timezone.now())

class ResultsView(generic.DetailView):
     model = Question
     template_name = "polls/results.html"



def vote(request , question_id):
    question = get_object_or_404(Question , pk=question_id)
    try:
        user_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, "polls/detail.html",
                            {"question": question,
                            "error_message": "You didn't select a choice."}
                        )
    else:
        user_choice.votes = F("votes") + 1
        user_choice.save() # save in DB 
        # This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



