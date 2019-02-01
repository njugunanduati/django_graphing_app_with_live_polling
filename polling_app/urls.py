from django.conf.urls import url, include
from django.contrib import admin
from polling_app.views import RandomNumberList
from polling_app.django_dash import DjangoDash


urlpatterns = [
    url(r'^polls/', RandomNumberList.as_view()),
    url(r'^home/', DjangoDash),
]
