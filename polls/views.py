from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse(
#         "hello, world. you're at the pools"
#         )
# def endex(request):
#     return HttpResponse(
#         "Its the end of the world i a now that"
#     )

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
