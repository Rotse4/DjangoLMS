# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from results.serializers import AnswerSerializer, QuizSerializer
from .models import Answer,Quiz
from django.db.models import Q

@api_view(['POST'])
def check_answer(request):
    if request.method == 'POST':
        answer_id = request.data.get('answer_id')
        try:
            answer = Answer.objects.get(id=answer_id)
        except Answer.DoesNotExist:
            return Response({"error": "Answer not found"}, status=status.HTTP_404_NOT_FOUND)

        if answer.is_correct:
            marks_awarded = 10 
            return Response({"message": "Correct answer!"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Incorrect answer!"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_questions(request):
    if request.method == 'GET':
        questions = Quiz.objects.all()
        serializer = QuizSerializer(questions, many=True)
        return Response({"data":serializer.data})
    


@api_view(["POST"])
def calc_marks(request):

    data ={}
    datad =request.data
    for q, value in enumerate(datad, start=1):
        data[q]=value
    print(data)
    serializer = QuizSerializer(data=request.data, many =True)


    if serializer.is_valid():
        serializer.save()
    return Response(serializer.errors)

@api_view(['POST'])
def submit_answer(request):
    received_data = request.data
    marks = 0
    print(received_data)
    for key in received_data:
        answer_id = int(key)
        # print(answer_id)
        find = Answer.objects.get(id=answer_id)

        if find.is_correct:
            marks+=1
            print("Awarded 1 mark for Answer ID:", answer_id)

    return Response({"You scored":marks})


@api_view(['POST'])
def answerss(request):
    if request.method == 'POST':
        # dict={}
        question_id_start = 1 
        dict = {i + question_id_start: text for i, text in enumerate(request.data)}
        print(dict)
        # print("dict " +str(request.data))
        dt={
            "question_id":request.data[0],
            "text":request.data[1]
        }
        print("my dt" +str(dt))
        print(dt["text"])
        # print(request.data)
        question_id = dt['question_id']
        # question_id = request.data.get('question_id')
        answer_id = dt['text']
        # answer_id = request.data.get('answer_id')
        question = Quiz.objects.get(id=question_id)
        answers = Answer.objects.filter(question=question, )
        correct_answer=Answer.objects.filter(question=question,is_correct=True )
        print("correct" +str(correct_answer))
        print("first answer" +str(correct_answer.first()))
        if (dt["text"]) == correct_answer.first().text:
            marks=+1
            print("amepata")
            print(marks)
        else:
            print("Amekosea")
        
        print(answers)

        return Response("good")
        # your_answer=(request.data["text"])
        # uganda_exists = any(answer.text == (request.data["text"]) for answer in answers)
        # print(uganda_exists)
        

        # # if not question_id or not answer_id:
        # if not question_id:
        #     return Response({"message": "Question ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        #     question = Quiz.objects.get(id=question_id)
        #     answer = Answer.objects.filter(id=answer_id, question=question).first()
        # except Quiz.DoesNotExist:
        #     return Response({"message": "Invalid question ID."}, status=status.HTTP_404_NOT_FOUND)
        # if not answer:
        #     return Response({"message": "Invalid answer ID."}, status=status.HTTP_404_NOT_FOUND)

        # if answer.is_correct:
        #     # Here, you could increment a score if you had a user's quiz attempt model.
        #     return Response({"message": "Correct answer!", "correct": True}, status=status.HTTP_200_OK)
        # else:
        #     return Response({"message": "Wrong answer.", "correct": False}, status=status.HTTP_200_OK)