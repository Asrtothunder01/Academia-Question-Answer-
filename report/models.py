from django.db import models
from answer.models import Answer
from question.models import Question
# Create your models here.
class Report(models.Model):
	answer = models.ForeignKey(Answer,on_delete = models.CASCADE)
	question = models.ForeignKey(Question,on_delete = models.CASCADE)
	report_response = models.TextField(blank = True)
	created_at = models.DateTimeField(auto_now = True)