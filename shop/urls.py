"""shop URL Configuration

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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




from django.contrib import admin
from django.urls import path, include

from order.views import CreateOrderView

schema_view = get_schema_view(
    openapi.Info(
        title='Python 15 shop',
        default_version = 'v1',
        description = 'Интернет магазин'
    ),
    public=True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/docs/', schema_view.with_ui('swagger')),

    path('api/v1/', include('account.urls')),
    path('api/v1/', include('product.urls')),
    path('api/v1/orders/', CreateOrderView.as_view())
]
