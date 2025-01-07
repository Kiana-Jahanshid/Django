from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from django.http import Http404
from django.template import loader # for loading html files
from django.urls import reverse 
from django.db.models import F
from django.utils import timezone
from .models import Question , Choice

# Create your views here.
# Numbers of pages in our website == Numbers of functions in this file
# for calling these functions , we should define route in polls/urls.py


def index(request):
    # will displays latest 5 polls questions , separated by commas , according to publication date.
    # " -publish_date " : means that print question based on published date,  in a descending order (newer question comes first)
    backend_list = Question.objects.filter(publish_date=timezone.now()).order_by("-publish_date")[:5] # will read five rows od DB 
    template = loader.get_template("polls/index.html") # load html file with loader 
    context = {"frontend_list": backend_list} # dictionary mapping template variable names to Python objects.
    return HttpResponse(template.render(context, request))
    # or return render(request, "polls/index.html", context)

def test(request):
    return HttpResponse("Hellooooo")

def detail(request , question_id):
    try:
        question = Question.objects.filter(pk=question_id)
    except Question.DoesNotExist:
        raise  Http404("Question does not exist ❌")
    return render(request, "polls/detail.html", {"question":question})


def results(request , question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


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



