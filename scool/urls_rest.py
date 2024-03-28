from django.urls import path, include
from rest_framework import routers
from .view_rest import *

router = routers.DefaultRouter()
# router = routers.SimpleRouter()
router.register(r'persons', PersonViewSet)
router.register(r'courses', CourseViewSet)



urlpatterns = [    
    path('v1/courses/', CourseAPIView.as_view()),
    path('v1/courses/<int:pk>/', CourseAPIView.as_view()),
    
    path('v2/courses/', CourseAPIView2.as_view() ),
    path('v2/courses/<int:pk>/', CourseApiUpdate.as_view() ),
    path('v2/coursedetail/<int:pk>/', CourseApiDetailView.as_view() ),
    
    path('v3/courses/', CourseViewSet.as_view({'get':'list','post':'create'}) ),
    path('v3/courses/<int:pk>/', CourseViewSet.as_view({'get':'retrieve'}) ),
    
    path('v3/scool-auth/', include('rest_framework.urls') ),

    path('v4/', include(router.urls) ),

]

# urlpatterns += router.urls