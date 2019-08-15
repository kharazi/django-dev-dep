import random
import uuid
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from users.serializers import UsersSerializer, RequestGetSerializer, RequestLoginSerializer, RequestSignupSerializer


class SignupView(APIView):

    def post(self, request):
        serializer = RequestSignupSerializer(data=request.data)
        if serializer.is_valid():
            u = serializer.save()
            print(u)
            return Response({
                'message': 'your account have been created successfuly',
                'data': serializer.data
            })
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



def login_view(request):
    if request.method == 'POST':
        serializer = RequestLoginSerializer(data=request.POST)
        if serializer.is_valid():
            u = authenticate(
                request,
                username=serializer.data['username'],
                password=serializer.data['password'])

            if u:
                print(u, request)
                login(request, u)
                return JsonResponse(
                    {
                        'message': 'Your account info is correct',
                        'data': {
                            'first_name': u.first_name,
                            "id": u.id,
                        }
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return JsonResponse(
                    {
                        'message': 'Your password is wrong'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            return JsonResponse(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class LoginView(APIView):

    def post(self, request):
        serializer = RequestLoginSerializer(data=request.data)
        if serializer.is_valid():
            # try:
            #     u = User.objects.get(
            #         username=serializer.data['username']
            #     )
            # except ObjectDoesNotExist:
                # return Response(
                #     {
                #         'message': 'There is not any account with this username'
                #     },
                #     status=status.HTTP_404_NOT_FOUND
                # ) 


            u = authenticate(
                request,
                username=serializer.data['username'],
                password=serializer.data['password'])

            if u is None:
                return Response(
                    {
                        'message': 'There is not any account with this username'
                    },
                    status=status.HTTP_404_NOT_FOUND
                ) 
            if u.check_password(serializer.data['password']):
                print(u)
                print(login(request, u))
                return Response(
                    {
                        'message': 'Your account info is correct',
                        'data': {
                            'first_name': u.first_name,
                            "id": u.id,
                        }
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'message': 'Your password is wrong'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class UserListItemView(APIView):

    def get(self, request):
        request_serializer = RequestGetSerializer(data=request.GET)
        if request_serializer.is_valid():

            users = User.objects
            if 'first_name' in request_serializer.data:
                users = users.filter(
                    first_name=request_serializer.data['first_name']
                )
            if 'last_name' in request_serializer.data:
                users = users.filter(
                    last_name=request_serializer.data['last_name']
                )

            serializer = UsersSerializer(instance=users, many=True)
            return Response(
                {
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                request_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        serializer = UsersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)

        return Response(
            {
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )
