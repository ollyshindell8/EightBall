from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from eightball.models import Answers

import random


class EightballAnswerView(ListView):
    model = Answers
    template_name = "return_answer.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        answers = Answers.objects.all()
        context['random_item'] = random.choice(answers)
        return context


class QuestionView(TemplateView):
    template_name = "question_form.html"


class IndexView(TemplateView):
    template_name = "index.html"

