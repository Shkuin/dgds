from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main"),
    path("upload/", views.game_uploading, name="upload"),
    path("catalog/", views.game_catalog, name="catalog"),
    path("catalog/<str:slug>/", views.game_detail, name="game_detail_url"),
    # path("js_script/<str:slug>/", views.game_detail, name="game_detail_url"),
]
