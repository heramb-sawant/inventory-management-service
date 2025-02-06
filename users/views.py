from django.http import HttpResponse
from django.shortcuts import render

from .models import Users


def get_users(request):
    most_recent = Users.objects.order_by("-id")[:5]
    context = {"latest_question_list": most_recent}
    return render(request, "users/index.html", context)


def get_user(request, user_id):
    return HttpResponse(f"User details to come! {user_id}")


def create_user(request):
    return HttpResponse("TODO:!")


def get_user_details(request, user_id):
    return HttpResponse(f"User details to come! {user_id}")
