from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('data_tk', views.DataTkViewSet)
router.register('daftar', views.DaftarViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]