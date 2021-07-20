from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(
        "hello, world. you're at the pools"
        )
def endex(request):
    return HttpResponse(
        "Its the end of the world i a now that"
    )

# Create your views here.
