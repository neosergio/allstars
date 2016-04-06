from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Comment
from .serializers import CommentSerializer
from employees.models import Category, Employee
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', ])
def comments(request, employee_id, category_id):
    if request.method == 'GET':
        employee = get_object_or_404(Employee, pk=employee_id)
        category = get_object_or_404(Category, pk=category_id)
        comments = get_list_or_404(Comment, to_user=employee, category=category)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)