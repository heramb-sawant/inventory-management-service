from django.urls import path


from . import views

urlpatterns = [
    path("", views.get_users, name="index"),
    path("<int:user_id>/", views.get_user, name="user"),
    path("<int:user_id>/details/", views.get_user_details, name="details"),
]
