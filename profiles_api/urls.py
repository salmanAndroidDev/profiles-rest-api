from django.urls import path, include
from profiles_api.views import HelloApiView, HelloViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name= 'Hello-viewset')

urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('', include(router.urls))
]
