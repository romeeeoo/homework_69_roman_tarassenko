import json

from django.http import JsonResponse
from django.views.generic import TemplateView


def add_view(request, *args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            a = float(data.get("A"))
            b = float(data.get("B"))
            result = a + b
            return JsonResponse({"result": result})
        except ValueError:
            response = JsonResponse({"error": "wrong type on input"})
            response.status_code = 400
            print(response.content)
            return response


def subtract_view(request, *args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            a = float(data.get("A"))
            b = float(data.get("B"))
            result = a - b
            return JsonResponse({"result": result})
        except ValueError:
            response = JsonResponse({"error": "wrong type on input"})
            response.status_code = 400
            print(response.content)
            return response


def multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            a = float(data.get("A"))
            b = float(data.get("B"))
            result = a * b
            return JsonResponse({"result": result})
        except ValueError:
            response = JsonResponse({"error": "wrong type on input"})
            response.status_code = 400
            print(response.content)
            return response


def divide_view(request, *args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            a = float(data.get("A"))
            b = float(data.get("B"))
            result = a / b
            return JsonResponse({"result": result})
        except ValueError:
            response = JsonResponse({"error": "wrong type on input"})
            response.status_code = 400
            print(response.content)
            return response
        except ZeroDivisionError:
            response = JsonResponse({"error": "zero division is not allowed"})
            response.status_code = 400
            print(response.content)
            return response


class CalculationsView(TemplateView):
    template_name = "calculations.html"
