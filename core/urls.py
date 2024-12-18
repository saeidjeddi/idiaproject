from django.urls import path, include
from django.contrib import admin

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('accounts.urls')),

]






urlpatterns += [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]