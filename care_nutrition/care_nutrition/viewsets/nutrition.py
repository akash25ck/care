from rest_framework import viewsets

from care_nutrition.models import (
    DoseRecord,
    GrowthAssessment,
    NutritionProgramme,
    SupplementationCourse,
)
from care_nutrition.serializers import (
    DoseRecordSerializer,
    GrowthAssessmentSerializer,
    NutritionProgrammeSerializer,
    SupplementationCourseSerializer,
)


class NutritionProgrammeViewSet(viewsets.ModelViewSet):
    queryset = NutritionProgramme.objects.all()
    serializer_class = NutritionProgrammeSerializer


class GrowthAssessmentViewSet(viewsets.ModelViewSet):
    queryset = GrowthAssessment.objects.all()
    serializer_class = GrowthAssessmentSerializer


class SupplementationCourseViewSet(viewsets.ModelViewSet):
    queryset = SupplementationCourse.objects.all()
    serializer_class = SupplementationCourseSerializer


class DoseRecordViewSet(viewsets.ModelViewSet):
    queryset = DoseRecord.objects.all()
    serializer_class = DoseRecordSerializer
