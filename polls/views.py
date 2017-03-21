from django.shortcuts import render
from django.http import HttpResponse

def details(request,question_id):
     return HttpResponse("Question: %s" %question_id)

def results(request,question_id):
      response="Results of Question: %s"
      return HttpResponse(response % question_id)

def vote(request,question_id):
      return HttpResponse("You're voting on question %s." % question_id)
