from django.db import models
# Create your models here.

class Question(models.Model):
	academic_session = models.IntegerField(default = 0)
	question_text = models.TextField(blank = True)
	updated_at = models.DateTimeField(auto_now = True)
	created_at  = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return self.question_text[:50]