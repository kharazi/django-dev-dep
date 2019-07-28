from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from users.models import Users, Message


def user_list(request):
    if request.method == 'GET':
        try:
            print(request.GET)
            query = request.GET['search']

            users = Users.objects.filter(first_name__startswith=query)
        except MultiValueDictKeyError:
            users = Users.objects.all()



        messages = Message.objects.all()
        for m in messages:
            print(
                m.sender,
                "->",
                m.receiver.first_name,
                ": ",
                m.text,
                m.date
            )
        # for m in messages:
        #     try:
        #         s = Users.objects.filter(id=m.sender)[0]
        #         r = Users.objects.filter(id=m.receiver)[0]
        #         print(
        #             s,
        #             "->",
        #             r,
        #             ": ",
        #             m.text,
        #             m.date
        #         )
        #     except IndexError:
        #         pass



        return render(
            request,
            'userlist.html',
            {
                "users": users,
            }
        )
    elif request.method == "POST":
        Users(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            number_of_friends=132
        ).save()
        users = Users.objects.all()
        return render(
            request,
            'userlist.html',
            {
                "users": users,
            }
        )
