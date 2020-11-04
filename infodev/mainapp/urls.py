from django.urls import path, include
from rest_framework import routers
from mainapp.views import WarningDeviceViewSet, MainView

router = routers.DefaultRouter()
router.register(r'devices', WarningDeviceViewSet, basename='devices')

app_name = 'main'

urlpatterns = [
    path('', MainView.as_view()),
    path('api/', include(router.urls)),
]
