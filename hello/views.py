from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz
import json
import os
from django.conf import settings


def index(request):
    return render(request, "landing.html")


def quiz_list(request):
    with open(os.path.join(settings.BASE_DIR, 'quiz.json'),
              encoding='utf-8') as file:
        data = json.load(file)

        for question in data["asks"]:

            Quiz.objects.create(
                ask=question["ask"],
                answer_one=question["answer_one"],
                answer_two=question["answer_two"],
                answer_three=question["answer_three"],
                answer_four=question["answer_four"],
                true_answer=question["true_answer"]
                )

    quiz = Quiz.objects.all()
    return render(request, "quiz.html", {"title": "Quizzes", "quiz": quiz})
