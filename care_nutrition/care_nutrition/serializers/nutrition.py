from rest_framework import serializers

from care_nutrition.models import (
    DoseRecord,
    GrowthAssessment,
    NutritionProgramme,
    SupplementationCourse,
)


class NutritionProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionProgramme
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "status",
            "created_at",
            "updated_at",
        ]


class GrowthAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrowthAssessment
        fields = [
            "id",
            "programme",
            "patient_id",
            "facility_id",
            "assessed_on",
            "weight_kg",
            "height_cm",
            "muac_cm",
            "oedema",
            "z_score",
            "notes",
            "created_at",
        ]


class SupplementationCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplementationCourse
        fields = [
            "id",
            "programme",
            "patient_id",
            "product_name",
            "start_date",
            "end_date",
            "status",
            "notes",
            "created_at",
        ]


class DoseRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoseRecord
        fields = [
            "id",
            "course",
            "given_on",
            "status",
            "quantity",
            "notes",
            "created_at",
        ]
