from django.db import models
from discussion.models import Discussion
# Create your models here.
class Post(models.Model):
	discussion = models.ForeignKey(Discussion,on_delete = models.CASCADE)
	content = models.TextField(blank = True)
