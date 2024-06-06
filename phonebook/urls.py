from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'contacts', views.ContactListView)
router.register(r'appinfo', views.AppInfoView)
router.register(r'profile', views.ProfileView)
router.register(r'register', views.RegisterView)
router.register(r'login', views.RegisterView)

urlpatterns = []

urlpatterns += router.urls