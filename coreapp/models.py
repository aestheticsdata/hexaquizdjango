from django.db import models

from datetime import datetime


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    registration_date = models.DateTimeField(default=datetime.now)
    last_activity = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username


class Question(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question, through='QuizQuestion')

    def __str__(self):
        return self.title


# Questions and Quizes have a many-to-many relationship, this table links Questions and Quizes together
class QuizQuestion(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=False)


class Score(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score_value = models.IntegerField(default=0)

    def __str__(self):
        return self.score_value


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
