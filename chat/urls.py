from django.urls import path
from . import views

urlpatterns = [
    path("", views.phones, name="phones"),
    path('online_users/', views.online_users, name='online_users'),
    path('contacts/', views.contact_list, name='contact_list'),

]