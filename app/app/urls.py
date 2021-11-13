"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from service import views as service_views
from api import views as api_views
from frontend import views as frontend_views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'resorts', api_views.ResortViewSet)
router.register(r'countries', api_views.CountryViewSet)
router.register(r'tours', api_views.TourViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', service_views.home, name='home'),
    path('signup/', service_views.signup, name='signup'),
    path('login/', service_views.login, name='login'),
    path('logout/', service_views.logout, name='logout'),
    path('landing', frontend_views.landing, name='landing'),
    #api
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
