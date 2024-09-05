from django.db import models
from question.models import  Question
# Create your models here.
class Answer(models.Model):
	question = models.ForeignKey(Question,on_delete = models.CASCADE)
	answer_text = models.TextField(blank = True)
	answer_file = models.CharField(max_length = 255, blank = True)
	updated_at = models.DateTimeField(auto_now = True)
	created_at = models.DateTimeField(auto_now = True)