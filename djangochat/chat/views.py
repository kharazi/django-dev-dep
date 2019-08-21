from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from chat.models import Messages, Conversations

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from chat.serializers import RequestChatSerializer, ResponseMessageListSerializer
from djangochat.utils import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication 
from django.contrib.auth.models import AnonymousUser



class MessageListView(APIView):

    def get(self, request):
        messages = Messages.objects.all()
        serializer = ResponseMessageListSerializer(
            messages,
            many=True
        )
        return Response(
            {
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )


class ChatView(APIView):

    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request):
        if type(request.user) is AnonymousUser:
            return Response({
                'message': 'Unauthorize!!!!'
            }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = RequestChatSerializer(
                data=request.data,
                context={
                    'user': request.user
                }
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'message': 'Message saved!'
                    }
                )
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )