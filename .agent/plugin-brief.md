# care_nutrition plugin brief

## Scope

`care_nutrition` is a two-sided CARE plugin for nutrition programmes. The first release
supports child growth monitoring and nutrition supplementation workflows without modifying
CARE core models or migrations.

The plugin owns its Django models, API, migrations, frontend bundle, navigation, and
translations. It may reference core patients, facilities, and encounters by foreign key,
but core must not reference the plugin.

## Product decisions for the MVP

- **Primary users:** facility staff responsible for nutrition screening and programme
  follow-up. Facility permissions remain the source of truth for staff access.
- **Patient portal:** not included in the MVP. Patient-facing access can be added later
  through deliberately read-only OTP-scoped endpoints.
- **Third-party services:** none.
- **Preview port:** `4173`.
- **Workspace:** keep the frontend plugin repository alongside the CARE checkouts, but place
  the backend plugin repository inside `$CARE_BE/care_nutrition` before registering it locally.
  A local `Plug` with `version=""` resolves that directory relative to `$CARE_BE`, and Docker
  only includes the CARE checkout in its build context.

These are implementation assumptions for the first build and should be confirmed before
production rollout, especially the target age range, measurement protocol, and reporting
requirements.

## Domain model

### Nutrition programme

An administratively configured programme belonging to a facility or organisation.
It defines the supported supplementation products, schedule, and active date range.

### Growth assessment

A dated observation for a patient, recording the measurement type and value with the
measurement unit and provenance. The MVP should support weight, height/length, MUAC, and
oedema status, while keeping the model extensible for additional indicators.

Assessments reference the core patient and facility and are immutable after capture except
for an explicit correction workflow. Derived classifications (for example, normal,
moderate acute malnutrition, or severe acute malnutrition) must be calculated from the
configured standard and retained with the observation so historical results remain
auditable.

### Supplementation course and dose

A course links a patient to a nutrition programme and records the indication, start/end
dates, product, planned frequency, and status. Individual doses record what was scheduled,
dispensed, administered, missed, or refused, together with the date, quantity, and staff
member.

The initial status set is `active`, `completed`, `paused`, and `stopped`. Staff with
programme-management permission may start, pause, resume, complete, or stop a course;
ordinary programme staff may record assessments and doses but may not change programme
configuration.

## API and authorization shape

The backend package is `care_nutrition`, mounted by CARE at `/api/care_nutrition/`.
Expected initial resources are:

| Resource | Staff operations |
| --- | --- |
| `programmes` | List/retrieve; manage only with programme-management permission |
| `assessments` | List/create/retrieve/correct within authorized facilities |
| `courses` | List/create/retrieve/update status within authorized facilities |
| `doses` | List/create/retrieve/update recording fields within authorized facilities |
| `config/` | Return client-safe feature and measurement configuration |

Every queryset must exclude soft-deleted rows and be scoped by the caller's facility or
organisation permissions. Patient identifiers and measurements must not be exposed outside
authorized staff routes in the MVP.

## Frontend surface

Use a standalone federated frontend package named `care_nutrition_fe`.

- Add a nutrition programme navigation item and routes for programme list/detail.
- Put patient-specific growth and supplementation actions behind existing patient
  extension points where available; prefer `routes` and `PatientHomeActions` before adding
  any core extension point.
- Provide an assessment entry form, growth history, supplementation course timeline, and
  dose recording flow.
- Keep all user-facing strings under the `nutrition__` i18n namespace and scope styles
  under `care-nutrition-container`.

## Delivery order

1. Scaffold `care_nutrition` and `care_nutrition_fe` from the templates.
2. Implement and migrate the backend models.
3. Add serializers, permission-scoped viewsets, URLs, and focused backend tests.
4. Verify the API with a staff token before building the frontend.
5. Add frontend types, API client, routes, forms, and translations.
6. Run backend tests, frontend type-check/build, and an end-to-end staff happy path.

## Core-diff policy

Do not edit `care` or `care_fe` unless an existing route, navigation item, or extension
point cannot host the feature. If a core change becomes necessary, it must be a generic
plugin extension point and must be documented separately in `.agent/core-diff.md`.
