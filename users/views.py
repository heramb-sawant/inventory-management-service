from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import QuerySet

from .models import Users


class IndexView(generic.ListView):
    template_name = "users/index.html"
    context_object_name = "most_recent"

    def get_queryset(self) -> QuerySet[Users, Users]:
        return Users.objects.order_by("-id")[:5]


def get_users(request: HttpRequest) -> HttpResponse:
    most_recent = Users.objects.order_by("-first_name")[:5]
    context = {"most_recent": most_recent}
    return render(request, "users/index.html", context)


def get_user(request: HttpRequest, user_id: str) -> HttpResponse:
    user = get_object_or_404(Users, pk=user_id)
    context = {"user": user}
    return render(request, "users/details.html", context)

    # try:
    #     user = Users.objects.get(pk=user_id)
    # except Users.DoesNotExist:
    #     raise Http404("User does not exist")
    # return render(request, "users/detail.html", {"user": user})


def create_user(request: HttpRequest, user_id: str) -> HttpResponse:
    return HttpResponse(f"User details to come! {user_id}")
    # question = get_object_or_404(Question, pk=question_id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST["choice"])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(
    #         request,
    #         "polls/detail.html",
    #         {
    #             "question": question,
    #             "error_message": "You didn't select a choice.",
    #         },
    #     )
    # else:
    #     selected_choice.votes = F("votes") + 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


# TODO: Find some good standards around error handling from models, request.get etc...
def update_user(request: HttpRequest, user_id: str) -> HttpResponse:
    user = get_object_or_404(Users, pk=user_id)
    updated_first_name = request.GET["first_name"]
    updated_last_name = request.GET["last_name"]
    if updated_first_name:
        user.first_name = updated_first_name

    if updated_last_name:
        user.last_name = updated_last_name

    user.save()

    return HttpResponseRedirect(reverse("users:details", args=[user.id]))
