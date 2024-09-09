from django.urls import path

from . import views

app_name = "todos"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="details"),
    path("create/", views.create, name="create"),
]
