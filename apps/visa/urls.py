from rest_framework.routers import DefaultRouter

from .viewsets import (
    CountryViewSet,
    DocumentViewSet,
    MediaViewSet,
    FAQViewSet,
    ContactRequestViewSet,
    AboutViewSet
)

router = DefaultRouter()
router.register("countries", CountryViewSet)
router.register("documents", DocumentViewSet)
router.register("medias", MediaViewSet)
router.register("faqs", FAQViewSet)
router.register("contact", ContactRequestViewSet)
router.register("about", AboutViewSet)

urlpatterns = router.urls
