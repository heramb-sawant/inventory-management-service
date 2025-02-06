from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Users


def get_users(request):
    most_recent = Users.objects.order_by("-id")[:5]
    context = {"most_recent": most_recent}
    return render(request, "users/index.html", context)


def get_user(request, user_id):
    user = get_object_or_404(Users, pk=user_id)
    context = {"user": user}
    return render(request, "users/details.html", context)

    # try:
    #     user = Users.objects.get(pk=user_id)
    # except Users.DoesNotExist:
    #     raise Http404("User does not exist")
    # return render(request, "users/detail.html", {"user": user})


def create_user(request):
    return HttpResponse("TODO:!")


def update_user(request, user_id):
    return HttpResponse(f"User details to come! {user_id}")
