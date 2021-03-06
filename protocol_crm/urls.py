from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [

    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')),

    # Local apps
    path('accounts/', include('users.urls')),
    path('', include('pages.urls')),
    path('orders/', include('orders.urls')),
    path('properties/', include('properties.urls')),
    path('tenants/', include('tenants.urls')),
    path('contracts/', include('contracts.urls')),
    path('owner/', include('owners.urls')),
    path('payments/', include('payments.urls')),
    path('emails/', include('emails.urls')),
    path('account/',include('accounts.urls')),
    path('creating_user/',include('creating_user.urls')),

    # API (v1)
    path('api/v1/', include('sms.api.urls')),
    path('api/v1/', include('properties.api.urls')),
    path('api/v1/', include('tenants.api.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
