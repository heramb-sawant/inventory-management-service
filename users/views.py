from django.http import HttpResponse


def get_users(request):
    return HttpResponse("User list to come!")
