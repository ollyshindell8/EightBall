from django.urls import path

from eightball.views import EightballAnswerView, QuestionView, IndexView

urlpatterns = [
    path('answer/', EightballAnswerView.as_view(), name='answer'),
    path('question/', QuestionView.as_view(), name='question'),
    path('', IndexView.as_view(), name='home')
]