from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz
import json
import os
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def index(request):
    return render(request, "landing.html")


def quiz_list(request):
    if(not Quiz.objects.all()):
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

    question_list = Quiz.objects.all()

    paginator = Paginator(question_list, 1) 

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        quiz = paginator.page(page)
    except (EmptyPage, InvalidPage):
        quiz = paginator.page(paginator.num_pages)

    return render(request, "quiz.html", {"title": "Quizzes", "quiz": quiz})
