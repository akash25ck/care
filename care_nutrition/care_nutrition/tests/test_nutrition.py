from django.test import SimpleTestCase

from care_nutrition.models import (
    DoseRecord,
    GrowthAssessment,
    NutritionProgramme,
    SupplementationCourse,
)
from care_nutrition.settings import plugin_settings


class NutritionPluginConfigurationTests(SimpleTestCase):
    def test_plugin_defaults(self):
        self.assertTrue(plugin_settings.NUTRITION_ENABLED)
        self.assertEqual(plugin_settings.NUTRITION_DEFAULT_PROGRAMME, "mnch")

    def test_model_names(self):
        programme = NutritionProgramme(name="Child Growth", slug="child-growth")
        self.assertEqual(str(programme), "Child Growth")

        assessment = GrowthAssessment(
            patient_id="PAT-001",
            facility_id="FAC-001",
            assessed_on="2026-01-01",
        )
        self.assertEqual(str(assessment), "PAT-001 on 2026-01-01")

        course = SupplementationCourse(
            patient_id="PAT-001",
            product_name="Ready-to-use Supplement",
            start_date="2026-01-01",
        )
        self.assertEqual(str(course), "PAT-001 - Ready-to-use Supplement")

        dose = DoseRecord(course=course, given_on="2026-01-02", quantity=1)
        self.assertIn("PAT-001", str(dose))
