from django.urls import path
from .views import *

urlpatterns = [
    path("", track_list, name="track_list"),
    path("Add/", create_track, name="create_track"),
    path("Update/<int:id>", update_track, name="update_track"),
    path("Delete/<int:id>", delete_track, name="delete_track"),
    path("Details/<int:id>", track_details, name="track_details"),
]
