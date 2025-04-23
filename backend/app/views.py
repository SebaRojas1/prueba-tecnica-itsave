from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

# Get all tasks
@api_view(['GET'])
def get_all_tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

# Create a new task
@api_view(['POST'])
def add_task(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a specific task
@api_view(['DELETE'])
def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Mark a task as completed
@api_view(['PATCH'])
def mark_task_completed(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    task.is_completed = not task.is_completed
    task.save()
    serializer = TaskSerializer(task)
    return Response(serializer.data)