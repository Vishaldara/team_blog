from django.conf.urls import url, include
import views

urlpatterns = [

    url(r'^$', views.listofposts),
    url(r'^(?P<id>\d+)/$', views.postdetail, name="postdetail"),
]