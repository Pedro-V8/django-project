from django.urls import path
from .views import UserView , UserDetail , LoginView

urlpatterns = [
    path('', UserView.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
    path('login/' , LoginView.as_view())
]