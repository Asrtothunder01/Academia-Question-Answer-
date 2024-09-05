from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Department
from .serializers import DepartmentSerializer
# Create your views here.

class DepartmentListView(APIView):
	@extend_schema(
	responses = DepartmentSerializer (many = True)
	
	)
	def get (self, request):
		department = Department.objects.all()
		serializer = DepartmentSerializer (department,many = True)
		return Response (serializer.data)
		