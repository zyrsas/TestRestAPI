from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from tests.models import Test, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer1', 'answer2', 'answer3', 'answer4', 'is_correct')


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=False)

    class Meta:
        model = Question
        fields = ('question', 'answer')


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    user = StringRelatedField(many=False)

    class Meta:
        model = Test
        fields = ('id', 'title', 'questions', 'user')







