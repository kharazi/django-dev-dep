from datetime import datetime
from users.models import Users
from django.http.response import JsonResponse



def user_list_item_view(request):
    if request.method == 'GET':
        user_list = []

        users = Users.objects

        if 'first_name' in request.GET:
            users = users.filter(
                    first_name=request.GET['first_name'])

        if 'last_name' in request.GET:
            users = users.filter(last_name=request.GET['last_name'])

        if 'first_name' not in request.GET and 'last_name' not in request.GET:
            users = []

        

        # Users.objects.filter(first_name=request.GET['first_name']).fileter(
        #     last_name=request.GET['last_name']
        # )

        # if 'first_name' in request.GET and 'last_name' in request.GET:
        #     users = Users.objects.filter(
        #         first_name=request.GET['first_name'],
        #         last_name=request.GET['last_name']
        #     )
        # elif 'first_name' in request.GET and not 'last_name' in request.GET:

        #     users = Users.objects.filter(
        #         first_name=request.GET['first_name']
        #     )
        for u in users:
            user_list.append(
                {
                    'first_name': u.first_name,
                    'last_name': u.last_name,
                    'id': u.id
                }
            )

        return JsonResponse(
            {
                'data': user_list
            }
        )
    elif request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        number_of_friends = request.POST['number_of_friends']
        birthday = datetime.fromisoformat(
            request.POST['birthday']
        )
        try:
            number_of_friends = int(number_of_friends)
        except ValueError:
            return JsonResponse({
                'message': 'number of freinds must be an integer field'
            }, status=400)

        if len(first_name) > 100:
            return JsonResponse({
                'message': 'first name must be less than 100 chars'
            }, status=400)

        u = Users(
            first_name=first_name,
            last_name=last_name,
            number_of_friends=number_of_friends,
            birthday=birthday
        )
        # u.full_clean()
        u.save()

        return JsonResponse(
            {
                'data': {
                    'first_name': u.first_name,
                    'last_name': u.last_name,
                    'birthday': u.birthday,
                    '#friends': u.number_of_friends,
                    'id': u.id
                }
            }
        )