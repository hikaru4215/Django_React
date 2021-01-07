from django.urls import path
from task.api import views

urlpatterns = [
    path('task/', views.ListView.as_view(), name="list"),
    path('task/<int:pk>/', views.DetailView.as_view(), name="detail")
]