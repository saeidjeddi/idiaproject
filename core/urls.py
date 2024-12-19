from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from core.settings.dev import DEBUG
from django.conf.urls.static import static



from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('accounts.urls')),
    path('blog/', include('blog.urls')),

]


urlpatterns += [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]


if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

