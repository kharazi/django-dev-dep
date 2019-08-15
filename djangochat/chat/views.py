from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from chat.models import Messages, Conversations

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from chat.serializers import RequestChatSerializer


class ChatView(APIView):

    def post(self, request):
        print(request.user)
        print('-------')
        serializer = RequestChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'Message saved!'
                }
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )