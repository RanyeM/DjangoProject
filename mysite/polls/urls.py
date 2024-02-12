from django.urls import path, include

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('messages/', views.MessageListView.as_view(), name='message-list'),
    path('messages/create/', views.MessageCreateView.as_view(), name='message-create'),
    path("polls/", include("polls.urls")),
]