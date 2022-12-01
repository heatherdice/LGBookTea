from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"), # path, url, name
    # insert more paths here
]
