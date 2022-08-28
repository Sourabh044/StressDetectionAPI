from django.urls import path , include
from rest_framework import routers
from .serializers import PredictSerializer
from .views import predict

router = routers.DefaultRouter()
# router.register(r'predict/',predict, basename = 'predict')
# from .views import 

urlpatterns = [
    path('',include(router.urls) ),
    path('check', predict, name = 'viewtera' ),
]