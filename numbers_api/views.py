import json

from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView


# from django.utils.datetime_safe import datetime


# Create your views here.
def echo(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
    }
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(f'Not allowed Method {request.method}')


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
