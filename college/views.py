from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import College
from .serializers import CollegeSerializer
# Create your views here.
class  CollegeCreateView(APIView):
	@extend_schema(
	responses = CollegeSerializer (many = True)
	)
	def get (self, request):
		Colleges = College.objects.all()
		serializer= CollegeSerializer(Colleges, many =True)
		return Response (serializer.data)
	