from django.db import models


class NutritionProgramme(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        ARCHIVED = "archived", "Archived"

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class GrowthAssessment(models.Model):
    programme = models.ForeignKey(
        NutritionProgramme,
        on_delete=models.CASCADE,
        related_name="assessments",
    )
    patient_id = models.CharField(max_length=64)
    facility_id = models.CharField(max_length=64)
    assessed_on = models.DateField()
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    muac_cm = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    oedema = models.BooleanField(default=False)
    z_score = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-assessed_on", "-created_at"]

    def __str__(self) -> str:
        return f"{self.patient_id} on {self.assessed_on}"


class SupplementationCourse(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        PAUSED = "paused", "Paused"
        COMPLETED = "completed", "Completed"
        STOPPED = "stopped", "Stopped"

    programme = models.ForeignKey(
        NutritionProgramme,
        on_delete=models.CASCADE,
        related_name="courses",
    )
    patient_id = models.CharField(max_length=64)
    product_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-start_date", "-created_at"]

    def __str__(self) -> str:
        return f"{self.patient_id} - {self.product_name}"


class DoseRecord(models.Model):
    class Status(models.TextChoices):
        SCHEDULED = "scheduled", "Scheduled"
        GIVEN = "given", "Given"
        MISSED = "missed", "Missed"
        REFUSED = "refused", "Refused"

    course = models.ForeignKey(
        SupplementationCourse,
        on_delete=models.CASCADE,
        related_name="doses",
    )
    given_on = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.SCHEDULED,
    )
    quantity = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["given_on", "created_at"]

    def __str__(self) -> str:
        return f"{self.course} on {self.given_on}"
