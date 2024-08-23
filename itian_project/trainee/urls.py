from django.urls import path
from .views import *

urlpatterns = [
    path("", trainee_list, name="trainee_list"),
    path("Add/", create_trainee, name="trainee_create"),
    path("Update/<int:id>", update_trainree, name="trainee_update"),
    path("Delete/<int:id>", delete_trainee, name="trainee_delete"),
    path("Details/<int:id>", trainee_details, name="trainee_details"),
]
