from django.urls import path
from views import (
    RowListView,
    RowDetailView,
    RowSessionDetailView,
    RowSessionCreateView,
    RowSessionUpdateView,
    PlayerCreateView,
    PlayerUpdateView,
    make_throws
)
urlpatterns = [
    path("row/", RowListView.as_view(), name="row-list" ),
    path(
        "row/<int:pk>",
        RowDetailView.as_view(),
        name="row-detail"
    ), path(
        "row_session/create",
        RowSessionCreateView.as_view(),
        name="row_session-create"
    ), path(
        "row_session/<int:pk>/update",
        RowSessionUpdateView.as_view(),
        name="row_session-update"
    ), path(
        "row_session/<int:pk>",
        RowSessionDetailView.as_view(),
        name="row_session-detail"
    ), path(
        "row_session/<int:pk>/throws",
        make_throws,
        name="row_session-throws"
    ), path(
        "player/create",
        PlayerCreateView.as_view(),
        name="player-create"
    ), path(
        "player/<int:pk>/update",
        PlayerUpdateView.as_view(),
        name="player-update"
    )
]
