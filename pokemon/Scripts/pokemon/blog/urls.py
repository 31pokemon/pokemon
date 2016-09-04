from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'new/$',views.post_new,name='post_new'),
	url(r'^(?P<pk>[0-9])/$',views.post_detail,name='post_detail'),
	url(r'^(?P<pk>[0-9])/edit/$',views.post_edit,name='post_edit'),
	url(r'^(?P<pk>[0-9])/delete/$',views.post_delete,name='post_delete')
]