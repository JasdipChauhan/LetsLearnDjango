from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^courses/', include('courses.urls')),
    url(r'^$', views.course_list),
]