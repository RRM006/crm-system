from rest_framework.routers import DefaultRouter
from .views import LeadViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'leads', LeadViewSet, basename='lead')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = router.urls
