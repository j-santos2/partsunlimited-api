from django.urls import path

from .views import *

app_name = "parts_api"

urlpatterns = [
    path("", PartViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "<int:pk>/",
        PartViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path("top-words", PartViewSet.as_view({"get": "top_words"})),
]
