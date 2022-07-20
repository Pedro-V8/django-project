from django.urls import path
from .views import UserView , UserDetail , LoginView, RegisterUserView

urlpatterns = [
    path('', UserView.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
    path('register/', RegisterUserView.as_view()),
    path('login/' , LoginView.as_view() , name='login')
]