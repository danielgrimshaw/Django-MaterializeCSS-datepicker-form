from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.ExampleModelCreate.as_view(), name='create'),
        url(r'^(?P<pk>[0-9]+)/$', views.ExampleModelUpdate.as_view(), name='edit'),
]
