from rest_framework import routers
from .viewsets import EmpanadaViewSet

router = routers.SimpleRouter()
router.register("empanada-api", EmpanadaViewSet)