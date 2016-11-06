from rest_framework.routers import DefaultRouter

from sketchfab.views import UserViewSet, Model3dViewSet, BadgeViewSet

__author__ = 'Pierre Rodier | pierre@buffactory.com'


router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
router.register(r'model3ds', Model3dViewSet, base_name='model3d')
router.register(r'badges', BadgeViewSet, base_name='badge')
urlpatterns = router.urls

