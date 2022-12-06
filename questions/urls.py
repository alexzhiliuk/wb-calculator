from django.urls import path

from . import views

urlpatterns = [
    path('send/', views.send_question, name='send_question'),
    path('send/response/<int:uid>/', views.send_question_response, name='send_question_response'),
]