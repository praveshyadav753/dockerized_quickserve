from django.contrib import admin
from django.urls import path
from .views import AddServiceView,DeleteServiceView


urlpatterns = [
    path("addservice/", AddServiceView.as_view(), name="addservice"),
    path("services/<int:service_id>/", DeleteServiceView.as_view(), name="delete-service"),

]