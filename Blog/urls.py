from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Core.views import robots, PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('',include('Core.urls')),
    path('robots.txt',robots)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]