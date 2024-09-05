from .models import Answer
from rest_framework import serializers

class AnswerSerializer (serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ['id','question','answer_text','answer_file']