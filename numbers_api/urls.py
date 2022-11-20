from django.urls import path

from numbers_api.views import echo, get_token_view, CalculationsView, add_view

urlpatterns = [
    path('echo/', echo, name="echo"),
    path('get-token/', get_token_view, name="get_token"),
    path('calc/', CalculationsView.as_view(), name="calculations"),
    path('add/', add_view, name="add"),
    # path('calc/', CalculationsView.as_view(), name="calculations"),
    # path('calc/', CalculationsView.as_view(), name="calculations"),
    # path('calc/', CalculationsView.as_view(), name="calculations"),
]
