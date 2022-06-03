from django.urls import path
from .views import PostsView, PostDetailView

urlpatterns = [
    path('', PostsView.as_view()),
    path('<int:pk>', PostDetailView.as_view())
]