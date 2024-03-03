# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from results.serializers import QuizSerializer
from .models import Answer,Quiz

@api_view(['POST'])
def check_answer(request):
    if request.method == 'POST':
        answer_id = request.data.get('answer_id')
        try:
            answer = Answer.objects.get(id=answer_id)
        except Answer.DoesNotExist:
            return Response({"error": "Answer not found"}, status=status.HTTP_404_NOT_FOUND)

        if answer.is_correct:
            return Response({"message": "Correct answer!"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Incorrect answer!"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_questions(request):
    if request.method == 'GET':
        questions = Quiz.objects.all()
        serializer = QuizSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)