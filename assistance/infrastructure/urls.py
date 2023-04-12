from django.urls import path

from assistance.infrastructure import views

urlpatterns = [
    path("", views.index, name="index"),
]