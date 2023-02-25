from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from questions.models import *
from questions.api.serializers import *


class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
