from django.urls import path, re_path

from chat.views import conversation_view

urlpatterns = [
    re_path('list/(?P<userparameter>\d{0,10})', conversation_view),
]
