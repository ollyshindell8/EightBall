from django.db import models


class Answers(models.Model):
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.answer


class NormalAnswers(models.Model):
    answer = models.CharField(max_length=50)

    def __str__(self):
        return self.answer

