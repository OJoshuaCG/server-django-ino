from rest_framework import routers
from .api import UsuarioViewSet, HogarViewSet, \
        DispositivoViewSet, ControlViewSet, InformeViewSet

# router = routers.DefaultRouter()
# router.register('api/usuarios', 
#         UsuarioViewSet, 'usuarios')
# router.register('api/hogares', 
#         HogarViewSet, 'hogares')
# router.register('api/dispositivos', 
#         DispositivoViewSet, 'dispositivos')
# router.register('api/controles', 
#         ControlViewSet, 'controles')
# router.register('api/informes', 
#         InformeViewSet, 'informes')

router = routers.DefaultRouter()
router.register('api/usuarios', UsuarioViewSet)
router.register('api/hogares', HogarViewSet)
router.register('api/dispositivos', DispositivoViewSet)
router.register('api/controles', ControlViewSet)
router.register('api/informes', InformeViewSet)


urlpatterns = router.urls
