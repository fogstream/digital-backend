from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from digital_backend.apps.suppliers.urls import router as suppliers_router
from digital_backend.apps.criteria.urls import router as criteria_router


class ExtendableRouter(routers.DefaultRouter):
    def extend(self, router):
        self.registry.extend(router.registry)
        self.urls.extend(router.urls)


client_router = ExtendableRouter()
client_router.extend(suppliers_router)

partner_router = ExtendableRouter()
partner_router.extend(suppliers_router)
partner_router.extend(criteria_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/api/', include(client_router.urls)),
    path('partner/api/', include(partner_router.urls))
]

if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title='B-clear API',
            default_version='v2',
            description='REST API глобальной системы поиска',
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += [
        path(r'^swagger(?P<format>\.json|\.yaml)$',
             schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger',
             schema_view.with_ui('swagger', cache_timeout=0),
             name='schema-swagger-ui'),
        path('redoc',
             schema_view.with_ui('redoc', cache_timeout=0),
             name='schema-redoc'),
        # path('silk/', include('silk.urls', namespace='silk'))
    ]
