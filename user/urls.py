from django.urls import path
from .views import UserView

urlpatterns = [
    path('', UserView.getUser, name="users"),
    path('add/', UserView.postUser, name="add")

]