from django.http import HttpResponse


def get_users(request):
    return HttpResponse("User list to come!")


def get_user(request, user_id):
    return HttpResponse(f"User get to come! {user_id}")


def get_user_details(request, user_id):
    return HttpResponse(f"User details to come! {user_id}")
