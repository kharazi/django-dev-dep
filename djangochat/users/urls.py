from django.urls import path, re_path

# from . import views
from . import views

urlpatterns = [
    # path('list/', views.user_list_view),
    path('item/', views.user_list_item_view)
]
