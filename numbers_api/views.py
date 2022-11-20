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
            my_sum = a + b
            return JsonResponse({"result": my_sum})
        except TypeError as e:
            response = JsonResponse({'error': f'{e}'})
            response.status_code = 400
            return response



class CalculationsView(TemplateView):
    template_name = "calculations.html"
