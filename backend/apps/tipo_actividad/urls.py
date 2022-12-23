from rest_framework.routers import SimpleRouter

from apps.tipo_actividad.views import TipoActividadView

tipo_actividad_router = SimpleRouter()
tipo_actividad_router.register('tipoactividades', TipoActividadView, basename='tipoactividades')
