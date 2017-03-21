from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Welcome.as_view(), name='welcome'),
	url(r'^quotes$', views.Quotes.as_view(), name='quotes'),
	url(r'^speakers$', views.Speakers.as_view(), name='speakers'),
	url(r'^categories/(?P<cat>\w+)$', views.Categories.as_view(), name='categories')
]