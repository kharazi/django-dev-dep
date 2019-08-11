import random 
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist

from users.models import Users

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


class LoginView(APIView):

    def post(self, request):
        serializer = RequestLoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                u = Users.objects.get(username=serializer.data['username'])
            except ObjectDoesNotExist:
                return Response(
                    {
                        'message': 'There is not any account with this username'
                    },
                    status=status.HTTP_404_NOT_FOUND
                ) 
            print(u.password)
            if serializer.data['password'] == u.password:
                random_token = random.randint(0, 100000)
                u.token = random_token
                u.save()
                return Response(
                    {
                        'message': 'Your account info is correct',
                        'data': {
                            'first_name': u.first_name,
                            "id": u.id,
                            'token': random_token
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

            users = Users.objects
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
