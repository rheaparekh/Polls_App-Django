from django.conf.urls import patterns, url
from polls import views

urlpatterns= patterns('',
  url(r'^$',views.index, name='index'),
  url(r'^(?P<question_id>\d+)/$',view.details,name='detail'),
  url(r'^(?P<question_id)\d+)/results/$',view.results,name='results'),
  url(r'^(?P<question_id>\d+)/vote/$',views.vote,name='vote'),
)
