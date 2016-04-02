from rest_framework import serializers
from .models import Employee


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('pk',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'level',
                  'current_month_score',
                  'last_month_score')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        depth = 1
        fields = ('pk',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'avatar',
                  'role',
                  'skype_id',
                  'last_month_score',
                  'current_month_score',
                  'level',
                  'total_score',
                  'categories',
                  'is_active',
                  'last_login')
