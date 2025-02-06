from django.urls import path


from . import views

# TODO: Take a look at class based views https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/
# Seems like a much simpler way to organize http methods without having to use different urls.
app_name = "users"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<str:user_id>/", views.get_user, name="details"),
    path("create/", views.create_user, name="create"),
    path("update/<str:user_id>/", views.update_user, name="update"),
]
