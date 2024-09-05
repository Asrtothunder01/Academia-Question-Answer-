from django.shortcuts import render
from  .models  import Answer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AnswerSerializer
from drf_spectacular.utils import extend_schema
# Create your views here.

class AnswerListView (APIView):
	@extend_schema(
	responses = AnswerSerializer (many = True)
	)
	
	def get (self, request):
		answer = Answer.objects.all()
		serializer = AnswerSerializer (answer,many = True)
		return Response (serializer.data)
