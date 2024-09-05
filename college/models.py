from django.db import models

# Create your models here.
class College(models.Model):
	college_name = models.CharField(max_length = 200, blank = True)
	def __str__(self):
		return self.college_name