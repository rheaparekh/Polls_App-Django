from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from polls.models import Question,Choice
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
def index(request):
     latest_question_list= Question.objects.order_by('-pub_date')[:5]
     question_list={'latest_question_list':latest_question_list}
     return render (request,'polls/index.html',question_list)

def details(request,question_id):
     question=get_object_or_404(Question,pk=question_id)
     return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
      question=get_object_or_404(Question,pk=question_id)
      return render(request, 'polls/results.html',{'question': question})

def vote(request,question_id):
       selected_question=get_object_or_404(Question,pk=question_id)
       try:  
           selected_choice =selected_question.choice_set.get(pk=request.POST['choice'])
       except( KeyError,Choice.DoesNotExist):
          return render(request, 'polls/detail.html',{
             'question':selected_question,
             'error_message':"Select a choice",
           })
       else:
          selected_choice.votes +=1
          selected_choice.save()
          return HttpResponseRedirect(reverse('polls:results',args=[selected_question.id]))
