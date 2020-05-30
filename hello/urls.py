from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='website-home'),
  path('quiz/', views.quiz_list, name='questions-quiz'),
]
