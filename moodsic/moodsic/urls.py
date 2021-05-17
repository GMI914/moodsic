from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required as lr
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),
    path('api/music/', include('music.urls')),
    path('openapi/',
         get_schema_view(
             title="Moodsic",
             description="API",
             authentication_classes=[SessionAuthentication],
             permission_classes=[IsAuthenticated],
         ),
         name='openapi-schema',
         ),

    path('swagger-ui/',
         lr(
             TemplateView.as_view(
                 template_name='swagger-ui.html',
                 extra_context={'schema_url': 'openapi-schema'}
             ),
         ), name='swagger-ui')
]

if settings.DEBUG:
    # -- Static Serving
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # -- Debug Toolbar
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
