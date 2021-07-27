from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
# def index(request):
#     return HttpResponse(
#         "hello, world. you're at the pools"
#         )
# def endex(request):
#     return HttpResponse(
#         "Its the end of the world i a now that"
#     )

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return HttpResponse(f"You're looking at question {question}")

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
