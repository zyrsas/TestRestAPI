from rest_framework import serializers
from rest_framework.relations import StringRelatedField, PrimaryKeyRelatedField
from tests.models import Test, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer1', 'answer2', 'answer3', 'answer4', 'is_correct')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question', 'answer')
    answer = AnswerSerializer(many=False)


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'title', 'questions', 'user')

    questions = QuestionSerializer(many=True)
    user = StringRelatedField(many=False)






