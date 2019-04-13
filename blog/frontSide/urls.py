from django.urls import path
from django.conf.urls import url
from . import views

# router=routers.DefaultRouter()
# router.register(r'users',UserViewSet)
urlpatterns = [
	path('',views.index,name="index"),
	url(r'^Post(?P<id>[0-9]+)/$',views.Post,name="Post")
	# url(r'',include(router.urls))
]