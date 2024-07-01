
from rest_framework.routers import DefaultRouter
from.views import GestionarActivos

# Crear una instancia del router y registrar nuestra vista
router = DefaultRouter()
router.register(r'entries', GestionarActivos, "GestionarActivos")

urlpatterns = router.urls