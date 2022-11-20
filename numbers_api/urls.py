from django.urls import path

from numbers_api.views import echo, get_token_view, CalculationsView, add_view, subtract_view, multiply_view, \
    divide_view

urlpatterns = [
    path('echo/', echo, name="echo"),
    path('get-token/', get_token_view, name="get_token"),
    path('calc/', CalculationsView.as_view(), name="calculations"),
    path('add/', add_view, name="add"),
    path('subtract/', subtract_view, name="subtract"),
    path('multiply/', multiply_view, name="multiply"),
    path('divide/', divide_view, name="divide")
]
