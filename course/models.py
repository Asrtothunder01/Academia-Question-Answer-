from django.db import models
from department.models import Department
# Create your models here.

class Course (models.Model):
	course_name = models.CharField(max_length = 200, blank = True)
	department = models.ForeignKey(Department,on_delete = models.CASCADE)
	
	def __str__(self):
		return self.course_name