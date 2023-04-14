from django.urls import path

from assistance.infrastructure import views

urlpatterns = [
    path("", views.assistance, name="assistance"),
]