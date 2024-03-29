from django.urls import path

from eightball.views import EightballAnswerView, QuestionView, IndexView, AboutView, NormalAnswerView

urlpatterns = [
    path('answer/', EightballAnswerView.as_view(), name='answer'),
    path('question/', QuestionView.as_view(), name='question'),
    path('', IndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('normal/', NormalAnswerView.as_view(), name='normal')
]