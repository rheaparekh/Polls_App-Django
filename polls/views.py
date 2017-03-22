from django.shortcuts import render
from django.http import HttpResponse,Http404
from polls.models import Question,Choice
from django.template import RequestContext, loader

def index(request):
     latest_question_list= Question.objects.order_by('-pub_date')[:5]
     question_list={'latest_question_list':latest_question_list}
     return render (request,'polls/index.html',question_list)

def details(request,question_id):
     return HttpResponse("Question: %s" %question_id)

def results(request,question_id):
      response="Results of Question: %s"
      return HttpResponse(response % question_id)

def vote(request,question_id):
      return HttpResponse("You're voting on question %s." % question_id)
