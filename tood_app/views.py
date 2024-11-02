from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ToDo
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def todo_list(request):
    if request.method == 'GET':
        todos = ToDo.objects.all().values()
        return JsonResponse(list(todos),safe = False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

@csrf_exempt
def create_todo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        todo = ToDo.objects.create(
            title=data['title'],
            description=data.get('description', ''),
            status=data.get('status', 'pending'),
            due_date=data.get('due_date')
        )
        return JsonResponse({'id': todo.id, 'message': 'ToDo created successfully!'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def todo_detail(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'GET':
        return JsonResponse({
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'status': todo.status,
            'due_date': todo.due_date,
            'created_at': todo.created_at,
            'updated_at': todo.updated_at,
        })
    elif request.method == 'PUT':
        data = json.loads(request.body)
        todo.title = data['title']
        todo.description = data.get('description', todo.description)
        todo.status = data.get('status', todo.status)
        todo.due_date = data.get('due_date', todo.due_date)
        todo.save()
        return JsonResponse({'message': 'Todo updated successfully!'})
    elif request.method == 'DELETE':
        todo.delete()
        return JsonResponse({'message': 'Todo deleted successfully!'})


