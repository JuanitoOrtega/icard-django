from django.contrib import admin
from django.urls import path, include
from django.conf import settings # para usar el media_root
from django.conf.urls.static import static # para usar el media_root
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.api.router import router_user
from categories.api.router import router_category
from products.api.router import router_product
from tables.api.router import router_table
from orders.api.router import router_order
from payments.api.router import router_payment

schema_view = get_schema_view(
    openapi.Info(
        title="iCard - ApiDocs",
        default_version='v1',
        description="Documentación de la API de iCard",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('users.api.router')),
    path('api/', include(router_user.urls)),
    path('api/', include(router_category.urls)),
    path('api/', include(router_product.urls)),
    path('api/', include(router_table.urls)),
    path('api/', include(router_order.urls)),
    path('api/', include(router_payment.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)