from django.urls import path, re_path, include

from . import views

app_name = "book"

urlpatterns = [
    re_path(r'^$',views.mainPage.as_view(),name="mainpage"),
]