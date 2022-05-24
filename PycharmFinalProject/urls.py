from django.contrib import admin
from django.urls import path, include
from book.views import *
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='Book')
router.register('journal', JournalViewSet, basename='Journal')
router.register('register', RegisterViewSet, basename='Register')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
]
