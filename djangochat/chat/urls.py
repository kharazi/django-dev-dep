from django.urls import path, re_path

from chat.views import ChatView

urlpatterns = [
    path('message/', ChatView.as_view())
]
