from django.urls import path
from .views import ProductView , ProductDetail

urlpatterns = [
    path('', ProductView.as_view()),
    path('<int:pk>/', ProductDetail.as_view()),
]