from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, HealthView

app_name = 'api'  

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')

urlpatterns = [
    path('', HealthView.as_view(), name='health'),
    path('', include(router.urls)),  
]
