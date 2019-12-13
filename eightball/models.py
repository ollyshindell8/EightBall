from django.db import models


class Answers(models.Model):
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.answer
