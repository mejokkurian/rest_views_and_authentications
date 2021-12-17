from django.urls import path
from django.urls.conf import include
from . import views
from .views import class_details
from .views import UserViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('class_details', class_details, basename='class_details')
router.register('UserViewset', UserViewset, basename='UserViewset')

urlpatterns = [
    path('api/',include(router.urls))

    
    # path('', views.post, name='index'),
    # path('details', views.details.as_view()),
    # path('class_details/<int:id>', views.class_details.as_view())
    
    
]