from django.urls import path, include
from rest_framework.routers import SimpleRouter
from django.conf import  settings
from django.conf.urls.static import static
from .views import (ProductViewSet, CategoryViewSet,
                    CommentViewSet)

router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)