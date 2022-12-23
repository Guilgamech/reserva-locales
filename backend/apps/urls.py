from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.actividad.views import ActividadView
from apps.area.views import AreaView
from apps.aseguramiento.views import AseguramientoView
from apps.local.views import LocalMedioView, LocalView, LocalReservacionView
from apps.medio.views import MedioView
from apps.reservacion.views import ReservacionView, ReservacionAseguramientoView
from apps.tipo_actividad.views import TipoActividadView
from apps.user.views import UserView, LogoutView


router = DefaultRouter()
router.register(prefix='tipo-actividad', viewset=TipoActividadView, basename='tipo_actividad')
router.register(prefix='medio', viewset=MedioView, basename='medio')
router.register(prefix='actividad', viewset=ActividadView, basename='actividad')
router.register(prefix='local', viewset=LocalView, basename='local')
router.register(prefix='local-medio', viewset=LocalMedioView, basename='local-medio')
router.register(prefix='local-reservacion', viewset=LocalReservacionView, basename='local-reservacion')
router.register(prefix='reservacion', viewset=ReservacionView, basename='reservacion')
router.register(prefix='reservacion-aseguramiento', viewset=ReservacionAseguramientoView,
                basename='reservacion-aseguramiento')
router.register(prefix='aseguramiento', viewset=AseguramientoView, basename='aseguramiento')
router.register(prefix='area', viewset=AreaView, basename='area')
router.register(prefix='users', viewset=UserView, basename='users')
router.register(prefix='token/logout', viewset=LogoutView, basename='token_logout')

app_name = 'api'
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/login/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]