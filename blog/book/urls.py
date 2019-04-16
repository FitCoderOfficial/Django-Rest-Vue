from rest_framework import routers

from .viewset import BookViewSet

router = routers.SimpleRouter()
router.register('book', BookViewSet)

urlpatterns = router.urls
