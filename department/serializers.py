from .models import Department
from rest_framework import serializers
class DepartmentSerializer (serializers.ModelSerializer):
	class Meta:
		model = Department
		fields = ['id','department_name','college_name']