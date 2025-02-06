from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Users


def get_users(request):
    most_recent = Users.objects.order_by("-id")[:5]
    context = {"latest_question_list": most_recent}
    return render(request, "users/index.html", context)


def get_user(request, user_id):
    user = get_object_or_404(Users, pk=user_id)
    return render(request, "users/detail.html", {"user": user})

    # try:
    #     user = Users.objects.get(pk=user_id)
    # except Users.DoesNotExist:
    #     raise Http404("User does not exist")
    # return render(request, "users/detail.html", {"user": user})


def create_user(request):
    return HttpResponse("TODO:!")


def get_user_details(request, user_id):
    return HttpResponse(f"User details to come! {user_id}")
