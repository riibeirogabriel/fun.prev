from django.db import models
import json
from django.conf import settings
import os

field_length = 500


class Person(models.Model):
    name = models.CharField(max_length=field_length)
    city = models.CharField(max_length=field_length)
    years_old = models.IntegerField()


class Quiz(models.Model):
    ask = models.CharField(max_length=field_length)
    answer_one = models.CharField(max_length=field_length)
    answer_two = models.CharField(max_length=field_length)
    answer_three = models.CharField(max_length=field_length)
    answer_four = models.CharField(max_length=field_length)
    true_answer = models.IntegerField()
