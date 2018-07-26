from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    time_of_creation = models.DateTimeField('Date Published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    clicks = models.IntegerField(default=0)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text



# Create your models here.
