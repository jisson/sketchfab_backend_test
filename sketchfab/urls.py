from rest_framework.routers import DefaultRouter

from sketchfab.views import UserViewSet, Model3dViewSet

__author__ = 'Pierre Rodier | pierre@buffactory.com'


router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
router.register(r'model3ds', Model3dViewSet, base_name='model3d')
urlpatterns = router.urls

# urlpatterns = patterns('sketchfab.views', )
