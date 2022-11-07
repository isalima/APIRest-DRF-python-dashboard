from .views import PessoasViewSet
from rest_framework.routers import DefaultRouter

app_name = 'core_api'

router = DefaultRouter()
router.register(r'pessoas', PessoasViewSet, basename='pessoa')

urlpatterns = router.urls
