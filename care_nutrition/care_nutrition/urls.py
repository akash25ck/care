"""URL routes.

Core mounts this module at /api/care_nutrition/ via the PLUGIN_APPS loop in
config/urls.py. Do not repeat that prefix here.
"""

from django.urls import path
from rest_framework.routers import DefaultRouter

from care_nutrition.viewsets.config import ConfigView
from care_nutrition.viewsets.nutrition import (
    DoseRecordViewSet,
    GrowthAssessmentViewSet,
    NutritionProgrammeViewSet,
    SupplementationCourseViewSet,
)

router = DefaultRouter()
router.register("programmes", NutritionProgrammeViewSet, basename="nutrition-programme")
router.register("assessments", GrowthAssessmentViewSet, basename="nutrition-assessment")
router.register("courses", SupplementationCourseViewSet, basename="nutrition-course")
router.register("doses", DoseRecordViewSet, basename="nutrition-dose")

urlpatterns = [
    *router.urls,
    path("config/", ConfigView.as_view(), name="care_nutrition-config"),
]
