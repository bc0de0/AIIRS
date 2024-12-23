from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root path points to hello_world view
]


