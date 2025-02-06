from django.urls import path


from . import views

app_name = "polls"
urlpatterns = [
    path("", views.get_users, name="index"),
    path("<int:user_id>/", views.get_user, name="details"),
    path("<int:user_id>/more/", views.get_user_details, name="more"),
]
