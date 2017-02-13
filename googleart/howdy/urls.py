# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^login/$', views.LoginPageView.as_view()),
    url(r'^register/$', views.RegisterPageView.as_view()),
]