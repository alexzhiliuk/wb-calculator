from rest_framework import serializers
from questions.models import *


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'user', 'text', 'status']

