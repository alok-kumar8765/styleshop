from django.urls import path,include
from app.api import views
from django.db import router
from rest_framework.authtoken.views import obtain_auth_token  
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from app.api.views import CustomerAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud',views.CustomerViewSet,basename='customer')
#router.register('crud',views.CustomerView,basename='customer')

urlpatterns =[
    path('api/',include(router.urls)),
    #path('demo/', views.CustomerView.as_view(), name='demo'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', CustomerAPIView.as_view(), name='user'),

    
]

'''
hit url : http://127.0.0.1:8000:/api/demo/
'''