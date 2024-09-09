from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, Http404
from todos.models import Todo
from django.views import generic

from django.db.models import F
from django.urls import reverse

# Create your views here.


class IndexView(generic.ListView):
    model = Todo
    template_name = "todos/index.html"


class DetailView(generic.DetailView):
    model = Todo
    template_name = "todos/details.html"


# def index(request: HttpRequest):
#     todos = Todo.objects.order_by("-created_at")

#     return render(request, "todos/index.html", {"todos": todos})


# def details(request: HttpRequest, id: int):
#     todo = get_object_or_404(Todo, pk=id)

#     return render(request, "todos/details.html", {"todo": todo})


def create(request: HttpRequest):
    try:
        title_input = request.POST["title"]
        body_input = request.POST["body"]

        if title_input.strip() == "":
            raise KeyError()

        todo = Todo()
        todo.title = title_input
        todo.body = body_input
        todo.save()

        return redirect("todos:index")

    except KeyError:
        return render(request, "todos/index.html", {"error_message": "Invalid todo"})
