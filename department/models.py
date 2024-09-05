from django.db import models
from college.models import College
# Create your models here.
class Department(models.Model):
	department_name = models.CharField(max_length = 200, blank = True)
	college_name = models.ForeignKey(College,null = True,on_delete =models.CASCADE)
	
	def __str__(self):
		return self.department_name