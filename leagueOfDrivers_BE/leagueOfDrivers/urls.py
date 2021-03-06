"""leagueOfDrivers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from wx_league import views
from wx_league import urls as user_urls
from share import urls as share_urls
from email_manage import urls as email_urls
from django.conf.urls.static import static
from . import settings
import xadmin


router = routers.DefaultRouter()
router.register(r'coupons', views.CouponsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('xadmin/', xadmin.site.urls),
    path('admin/', admin.site.urls),
    path('league/',include(user_urls)),
    path('email/',include(email_urls)),
    path('share/', include(share_urls)),
    path('api-auth/',include('rest_framework.urls', namespace = 'rest_framework')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
