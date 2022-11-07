from django.contrib import admin
from django.urls import path, include

from core_api.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('', include('core.urls', namespace='core')),

]
