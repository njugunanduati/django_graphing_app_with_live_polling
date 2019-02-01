from django.conf.urls import url, include
from django.contrib import admin
from polling_app.views import RandomNumberList, HomeView


urlpatterns = [
    url(r'^polls/', RandomNumberList.as_view()),
    url(r'^home/', HomeView.as_view()),
]
