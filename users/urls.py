from django.urls import path


from . import views

app_name = "users"
urlpatterns = [
    path("", views.get_users, name="index"),
    path("<str:user_id>/", views.get_user, name="details"),
    path("<str:user_id>/more/", views.get_user_details, name="more"),
]
