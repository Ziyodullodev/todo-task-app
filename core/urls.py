# from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
# from utils.swagger import schema_view
from django.urls import path, include
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('admin3/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    # path('rosetta/', include('rosetta.urls')),
]

urlpatterns += [
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('apps.task.urls')),
    path('api/', include('apps.users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
