from datetime import datetime

from users.models import Users
from django.http.response import JsonResponse

from users.serializers import UsersSerializer, RequestGetSerializer


def user_list_item_view(request):
    if request.method == 'GET':
        request_serializer = RequestGetSerializer(data=request.GET)
        if request_serializer.is_valid():

            users = Users.objects
            if request_serializer.data['first_name']:
                users = users.filter(
                    first_name=request_serializer.data['first_name']
                )
            if request_serializer.data['last_name']:
                users = users.filter(
                    last_name=request_serializer.data['last_name']
                )

            serializer = UsersSerializer(instance=users, many=True)
            return JsonResponse(
                {
                    'data': serializer.data
                }
            )
        else:
            return JsonResponse(
                request_serializer.errors,
                status=400
            )

    elif request.method == 'POST':
        serializer = UsersSerializer(data=request.POST)

        if serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status=400)

        return JsonResponse({
            'data': serializer.data
        })