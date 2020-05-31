from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Quiz
import json
import os
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.generic.base import TemplateView
from django.views.generic import View
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings


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


class ChatterBotAppView(TemplateView):
    template_name = 'app.html'


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })