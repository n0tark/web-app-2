from django.contrib import admin
from django.urls import path, include
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import phonebook
from phonebook.views import add_contact, edit_contact, delete_contact

schema_view = get_schema_view(
    openapi.Info(
        title="PhoneBook API",
        default_version='v1',
        description="API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="1@1.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url='https://virtserver.swaggerhub.com/vladsel/contacts/1.0.0',
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('phone-book/', include('phonebook.urls')),
    path('add/', add_contact, name='add_contact'),
    path('edit/<int:pk>/', edit_contact, name='edit_contact'),
    path('delete_contact/<int:pk>/', delete_contact, name='delete_contact'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("channel/", include("chat.urls")),
]


