from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Course
from .serializers import CourseSerializer
# Create your views here.

class CourseListView(APIView):
	@extend_schema(
	responses = CourseSerializer (many = True)
	)
	
	def get (self, request):
		course = Course.objects.all()
		serializer = CourseSerializer (course, many = True)
		return Response (serializer.data)