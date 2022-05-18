from django.urls import path
from .views import UserView , UserDetail

urlpatterns = [
    path('', UserView.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
]