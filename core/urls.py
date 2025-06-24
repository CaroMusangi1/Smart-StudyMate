from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload'),  # changed from views.home to views.upload_file
]
