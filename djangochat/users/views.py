from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

class User:
    
    def __init__(self, first_name, last_name, grades=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
        # return self.first_name + ' ' + self.last_name

    def get_fullname(self):
        return "%s %s" % (self.first_name, self.last_name)


users = [
    User('Vahid', 'Kharazi', [1, 2, 18]),
    User('Sara', 'Ahmadi', [4, 20, 15]),
    User('Tarane', 'Ali Doosti', [17, 7])
]

def search_query(query):
    result = []
    for u in users:
        if u.first_name == query:
            result.append(u)
    return result


def user_list(request):
    if request.method == 'GET':
        print(request.GET)
        try:
            q = request.GET['search']
            result = search_query(q)
        except MultiValueDictKeyError:
            result = users        
        return render(
            request,
            'userlist.html',
            {
                "users": result,
            }
        )
    elif request.method == 'POST':
        print('request.POST:', request.POST)
        new_user = User(
            first_name=request.POST['firstname'],
            last_name=request.POST['lastname'])
        users.append(new_user)
        return render(
            request,
            'success.html'
        )


# def user_list(request):
#     print(request.GET)
#     q = request.GET['search']
#     result = search_query(q)
#     return render(
#         request,
#         'userlist.html',
#         {
#             "users": result,
#         }
#     )

# def user_list(request):
#     response_text = ""
#     for u in users:
#         response_text += "<br/>"
#         response_text += u.get_fullname()
#     return render(
#         request,
#         'userlist.html',
#         {
#             "name": "Sara",
#             "users": users,
#             "text": response_text
#         }
#     )

# def user_list(request):
#     response_text = ""
#     for u in users:
#         response_text += "<br/>"
#         response_text += u.get_fullname()
#     return HttpResponse(
#         "<html> Salam, in list user hast: %s <html/>" % (response_text))