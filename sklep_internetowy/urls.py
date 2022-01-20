"""sklep_internetowy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import include, path
#from rest_framework import routers
#from sklep import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'sklep'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('koszyk/', include('koszyk.urls', namespace='koszyk')),
    path('zamowienia/', include('zamowienia.urls', namespace='zamowienia')),

    path('', include('sklep.urls', namespace='sklep')), #cos tu nie teges

    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('', views.product_list, name='product_list'),
    #path('<slug:category_slug>/', views.product_list(), name='product_list_by_category'), #usunac w razie w
    #path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'), #usunac w razei w

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
