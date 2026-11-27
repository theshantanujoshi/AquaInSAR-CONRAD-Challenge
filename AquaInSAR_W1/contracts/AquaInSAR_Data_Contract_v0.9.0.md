# AquaInSAR Data Contract v0.9.0 (Draft for W1 review)

**Contract ID:** `AQS-DC` · **Version:** `0.9.0` · **Version date:** 2026-11-24
**Revision date:** 2026-11-27 (unreleased draft corrections from PR review; v0.9.0 is not a released version)
**Owner:** AC (Aishwary) · **Reviewer:** SJ · **W1 review gate:** 2026-11-29 · **Promotion gate:** 2026-12-06
**Status code:** `DRAFT_FOR_W1_REVIEW`
**Machine-readable companion:** `AquaInSAR_Data_Contract_v0.9.0.json` (identical IDs, versions, fields and rules)

## 0. Why this is v0.9.0 and not v1.0

A v1.0 contract would assert a coherent initial specification. The repository does not support that assertion: AQ-01 (pilot region), AQ-03 (accessible reference data), AQ-04 (Sentinel-1 feasibility) and AQ-05 (CRS, grid, units, formats, vocabularies) are unresolved, and no real dataset, scene manifest or processed product exists locally. This document is therefore a **provisional pre-1.0 specification**: structure, validation rules and placeholders are defined; pilot-dependent values are explicitly `PENDING`. Promotion to v1.0 is a recorded decision at the 2026-12-06 gate, not an automatic step.

## 1. Scope and governing principles

### In scope
- Metadata and field specifications for prospective InSAR displacement, groundwater well and rainfall tables.
- Validation rules, error severities and reporting behaviour.
- Explicit placeholders for pilot-dependent spatial and temporal decisions.

### Out of scope
- Data acquisition, download or processing.
- Unit conversion, reprojection, interpolation, spatial joins and temporal resampling.
- Validation, risk classification, forecasting, alerts and dashboard behaviour.
- Competition submission requirements (AQ-02).

### Governing principles
1. ADR-0001: deformation is reported as a satellite-derived observation before any groundwater interpretation.
2. Claim levels: **Planned < Observed < Associated < Validated < Predicted**. This contract supports the first two only.
3. No assumption is converted into a confirmed project requirement.
4. Validation reports describe problems; they never edit, drop, clamp or impute input records.

### Evidence status of every dataset entry
`ANTICIPATED_SOURCE_IDENTIFIED` = a source link exists in project documents but no local data exist. `DEFERRED_PENDING_PILOT` = schema deferred until the pilot and geometry are decided. All five entries have `availability_status = NO_LOCAL_DATA`.

## 2. Global conventions

### 2.1 Missing values and reason codes
- The only accepted CSV null representation is an **empty field**.
- Numeric sentinel values (for example `-9999`) are **not** permitted as missing-value codes.
- Optional fields may be empty only with a recorded reason.
- `missing_reason` is a **single code valid only when every empty optional field in the row shares that reason**.
- When different optional fields are empty for different reasons, populate `missing_reason_map`: a JSON object mapping each empty field name to one of the controlled reason codes. The single `missing_reason` may then be empty.
- Controlled reason codes: `NOT_MEASURED`, `MASKED`, `UNAVAILABLE`, `INVALID`, `NOT_APPLICABLE`, `UNKNOWN`.
- Zero is a measurement, never a null code.

### 2.2 Timestamps
- Canonical representation: **ISO 8601**; preferred timezone **UTC** (`...Z` or `+00:00`).
- Date-only values (e.g. `2024-05-01`) are allowed with `temporal_precision = day`; no timezone is invented for them.
- `acquisition_date` (SAR scene) and `observation_date` (well/rainfall) are distinct concepts and must not share a column without a documented equivalence rule.
- Rainfall records carry explicit `period_start` and `period_end` dates defining the closed accumulation interval. `observation_date` is the source-reported observation/publication date and **must not be used alone for temporal matching**; matching uses `[period_start, period_end]`.
- Duplicate timestamps are handled by the unique constraints in §5, not by silently keeping one row.

### 2.3 Coordinates and CRS
- Axis order is **longitude (x), latitude (y)** — PROPOSED, pending AQ-05.
- Global validity ranges: longitude `[-180, 180]`, latitude `[-90, 90]`.
- Every dataset must declare its CRS explicitly. CRS is never inferred from coordinate magnitudes.
- The canonical project CRS is `null` / **PENDING** (AQ-05). Source CRS values are `PENDING` where not stated.
- W1 geometry scope is point coordinates and identifiers only. Boundaries, rasters and common grids are deferred.
- Invalid coordinates are reported with row numbers and are not repaired or removed.

### 2.4 Units
- Every measurement value has an explicit unit field. No implicit units; no automatic conversion.
- Proposed canonical units (**PROPOSED**, not approved): displacement `mm`, groundwater depth `m_bgl`, rainfall `mm`.
- Conversion is allowed only in a later contract version with a recorded formula, source unit, target unit and lineage.

### 2.5 Provenance and quality
- Required dataset metadata: `dataset_id`, `name`, `description`, `source_organisation`, `source_reference`, `spatial_coverage`, `temporal_coverage`, `spatial_resolution`, `temporal_resolution`, `data_format`, `availability_status`, `known_limitations`.
- Required record fields for all tabular datasets: `dataset_id`, `source_reference`, `processing_lineage`.
- Derived records must preserve input dataset id/version, code/config version, processing date, parameters and operator.
- Quality flags and uncertainty travel with measurements. If uncertainty is not quantified, leave `uncertainty_value` empty and explain via `missing_reason` / `uncertainty_method`; absence must not be read as certainty.
- **Value/quality semantics:** `quality_flag` states whether a measurement value is present and trustworthy. `VALID`, `LOW_COHERENCE`, `ATMOSPHERIC` and `QUESTIONABLE` require a value. `MASKED`, `INVALID`, `UNKNOWN` and `NOT_MEASURED` mean **no reliable value exists**: the measurement value field must be empty and a reason must be recorded (single code or map).
- Error severities: `ERROR` (schema contract violation) and `WARNING` (review needed, not necessarily invalid).

## 3. Dataset inventory

| ID | Name / description | Source organisation & location | Method | Spatial / temporal coverage | Resolution (spatial / temporal) | CRS | Format | Units / variables | Limitations | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `AQS-INSAR-S1-DISPLACEMENT` | Point/pixel displacement time series derived from Sentinel-1; derived measurement, not SLC imagery and not groundwater | ESA Copernicus Sentinel-1; processing route undecided; refs: `docs/independent-research.md`, MF inventory [S10], [S11] | SAR acquisition + interferometric time-series workflow; processor/config undecided | PENDING: bounded by AQ-01 and AQ-04 | PENDING / PENDING (revisit unverified for pilot) | PENDING; must be declared per dataset | CSV point/pixel series; rasters deferred | Proposed `mm`; `deformation_value`, `coherence`, `measurement_convention`, `quality_flag` | LOS is not automatically vertical; atmosphere/orbit/decorrelation/unwrapping; agricultural coherence unverified; no scene manifest | `ANTICIPATED_SOURCE_IDENTIFIED`, `NO_LOCAL_DATA` |
| `AQS-GW-CGWB-WELL` | Station-level groundwater level or piezometric head records; not an InSAR measurement or validation label by itself | CGWB / UP Ground Water Department; MF inventory [S1], [S3], [S4], [S5], [S6] | Monitoring-well measurement; source reports four seasonal readings/year | PENDING: assessment units/wells after AQ-01, AQ-03; source examples 2023-24 | Point / about 4 readings per year (source-reported, not confirmed locally) | PENDING (decimal degrees in source, CRS unstated) | CSV extracted from published PDFs; PDFs retained as source | Proposed `m_bgl`; `measurement_value`, `measurement_type`, `datum`, `screen_depth_m`, `aquifer` | 4 samples/year cannot establish a trend; datum/screen/aquifer/missing reasons not compiled; stage categories are not water levels | `ANTICIPATED_SOURCE_IDENTIFIED`, `NO_LOCAL_DATA` |
| `AQS-RAIN-IMD-DISTRICT` | Rainfall context; district aggregates may not match pilot boundary or wells | IMD / IMD-derived CGWB tables; MF inventory [S7] | Public statistics and year-book tables; exact files unselected | PENDING: station or district relative to pilot; multi-year archive, exact period unconfirmed | PENDING: station/district aggregate; monthly/seasonal/annual aggregation unconfirmed | PENDING | CSV extracted from public tables | Proposed `mm`; `rainfall_value`, `accumulation_period`, `source_spatial_support` | Spatial support unresolved; one year cannot establish climatology; station vs gridded provenance unknown | `ANTICIPATED_SOURCE_IDENTIFIED`, `NO_LOCAL_DATA` |
| `AQS-REF-HYDROGEOLOGY` | Aquifer and geological map context for deformation plausibility | CGWB NAQUIM / GSI; MF inventory [S8], [S9] | Published maps/reports; vector extracts not obtained | PENDING; report vintages 2017-2024 | PENDING: map scale/vector availability unverified | PENDING | TBD (vector or raster); reports retained | Variables anticipated: `lithology`, `aquifer_type`, `confinement`, `map_scale`, `source_year` | GSI access/license unverified; reports alone do not establish compaction | `DEFERRED_PENDING_PILOT`, `NO_LOCAL_DATA` |
| `AQS-REF-DEM` | Terrain reference for processing context; not an observation | USGS EarthExplorer / NASA SRTM; MF inventory [S21] | Public DEM download; product version unselected | Global; pilot extent PENDING | Nominal 90 m (screened, unverified) | PENDING | TBD (raster) | Proposed `m`; `elevation` | Coarse for local gradients; void filling/quality must be documented | `DEFERRED_PENDING_PILOT`, `NO_LOCAL_DATA` |

## 4. Schema specification — common type vocabulary

| Type | Parsing rule |
|---|---|
| `string` | Non-empty text; optional full-match `pattern` and/or `allowed_values`. |
| `date` | `YYYY-MM-DD` parseable as ISO 8601 date. |
| `datetime` | ISO 8601 with timezone offset; `Z` accepted. |
| `decimal` | Finite decimal number; `NaN`/`Infinity` rejected; optional `minimum`/`maximum`. |
| `integer` | Finite integer. |

Column names are case-sensitive and must match exactly. A field is **required** if the column must exist; **nullable** if empty values are allowed. `unit` describes the field's own unit, not the associated measurement's unit.

## 5. Schema specifications

### 5.1 `AQS-INSAR-S1-DISPLACEMENT`

Unique constraints: `observation_id`; `pixel_id + acquisition_date + relative_orbit + pass_direction` (tracks are not pooled silently). Unit pair: `deformation_value` → `deformation_unit`.

| Field | Type | Req. | Nullable | Unit | Constraint | Description | Provenance |
|---|---|---|---|---|---|---|---|
| `observation_id` | string | yes | no | — | pattern `^[A-Za-z0-9_.:-]+$` | Stable unique id for one displacement record | generated by processing run |
| `dataset_id` | string | yes | no | — | pattern `^AQS-[A-Z]+-[A-Z0-9-]+(-v[0-9]+\.[0-9]+\.[0-9]+)?$` | Source/derived dataset version id | contract |
| `pixel_id` | string | yes | no | — | — | Stable pixel or persistent-scatterer id | processing configuration |
| `longitude` | decimal | yes | no | degrees | [-180, 180] | X coordinate in declared CRS | processing geometry |
| `latitude` | decimal | yes | no | degrees | [-90, 90] | Y coordinate in declared CRS | processing geometry |
| `crs` | string | yes | no | — | explicit EPSG/WKT | CRS identifier; required even while canonical value is pending | dataset metadata |
| `acquisition_date` | date | yes | no | — | ISO 8601 date | SAR acquisition date; distinct from well observation date | scene metadata |
| `platform` | string | yes | no | — | `SENTINEL-1A`, `SENTINEL-1B`, `SENTINEL-1C` | Radar platform that acquired the scene | scene metadata |
| `relative_orbit` | integer | yes | no | — | 1–175 | Relative orbit; defines track with `pass_direction` | scene metadata |
| `pass_direction` | string | yes | no | — | `ASCENDING`, `DESCENDING` | Orbit direction; prevents silent track pooling | scene metadata |
| `polarization` | string | no | yes | — | `VV`, `VH`, `HV`, `HH`, `VV+VH` | Polarization channel where known | scene metadata |
| `incidence_angle` | decimal | no | yes | degrees | [0, 90] | Look incidence angle where known | processing geometry |
| `reference_date` | date | no | yes | — | ISO 8601 date | Date to which displacement is referenced | processing configuration |
| `measurement_convention` | string | yes | no | — | `LOS`, `VERTICAL`, `UNKNOWN` | Whether displacement is LOS, vertical or unknown | processing configuration |
| `deformation_value` | decimal | yes | conditional | see `deformation_unit` | finite; empty only for `MASKED`/`INVALID`/`UNKNOWN` | Displacement value; sign convention documented in lineage | processing output |
| `deformation_unit` | string | yes | no | — | — | Unit of deformation_value; no implicit conversion | processing output |
| `coherence` | decimal | no | yes | fraction | [0, 1] | Interferometric coherence where supplied | processing output |
| `quality_flag` | string | yes | no | — | `VALID`, `LOW_COHERENCE`, `ATMOSPHERIC`, `MASKED`, `INVALID`, `UNKNOWN` | Value-required vs no-value flag (see §2.5) | processing output |
| `uncertainty_value` | decimal | no | yes | same as deformation unit | ≥ 0 | Quantified uncertainty when available | processing output |
| `uncertainty_method` | string | no | yes | — | — | Method used, or NOT_QUANTIFIED | processing output |
| `missing_reason` | string | no | yes | — | controlled reason codes | Single code; valid only if all empty optional fields share it | producer |
| `missing_reason_map` | string | no | yes | — | JSON object of field→reason code | Per-field reasons when empty optional fields differ | producer |
| `source_reference` | string | yes | no | — | — | Exact source version link/citation | producer |
| `processing_lineage` | string | yes | no | — | — | Inputs, code/config version, parameters, date, operator | producer |

### 5.2 `AQS-GW-CGWB-WELL`

Unique constraints: `observation_id`; `station_id + observation_date`. Unit pair: `measurement_value` → `measurement_unit`.

| Field | Type | Req. | Nullable | Unit | Constraint | Description | Provenance |
|---|---|---|---|---|---|---|---|
| `observation_id` | string | yes | no | — | pattern `^[A-Za-z0-9_.:-]+$` | Stable unique id for one well observation | generated during ingest |
| `dataset_id` | string | yes | no | — | pattern `^AQS-[A-Z]+-[A-Z0-9-]+(-v[0-9]+\.[0-9]+\.[0-9]+)?$` | Dataset version id used for this record | contract |
| `station_id` | string | yes | no | — | — | Monitoring-well id as published | source table |
| `observation_date` | date | yes | no | — | ISO 8601 date | Date water level was observed | source table |
| `longitude` | decimal | yes | no | degrees | [-180, 180] | Well longitude in declared CRS | source table |
| `latitude` | decimal | yes | no | degrees | [-90, 90] | Well latitude in declared CRS | source table |
| `crs` | string | yes | no | — | explicit EPSG/WKT | CRS identifier | dataset metadata |
| `measurement_value` | decimal | yes | conditional | see `measurement_unit` | finite; empty only for `INVALID`/`UNKNOWN`/`NOT_MEASURED` | Depth or head; sign/origin depends on type | source table |
| `measurement_unit` | string | yes | no | — | — | Unit from source; no conversion | source table |
| `measurement_type` | string | yes | no | — | `WATER_LEVEL_DEPTH_BGL`, `PIEZOMETRIC_HEAD`, `UNKNOWN` | What the measurement represents | source metadata |
| `datum` | string | no | yes | — | — | Measurement/elevation datum if supplied | source metadata |
| `screen_depth_m` | decimal | no | yes | m | ≥ 0 | Well screen depth where known | source metadata |
| `aquifer` | string | no | yes | — | — | Aquifer or group tapped | source metadata |
| `quality_flag` | string | yes | no | — | `VALID`, `QUESTIONABLE`, `INVALID`, `UNKNOWN`, `NOT_MEASURED` | Value-required vs no-value flag (see §2.5) | source metadata |
| `missing_reason` | string | no | yes | — | controlled reason codes | Single code; valid only if all empty optional fields share it | producer |
| `missing_reason_map` | string | no | yes | — | JSON object of field→reason code | Per-field reasons when empty optional fields differ | producer |
| `source_reference` | string | yes | no | — | — | Exact publication/table id | producer |
| `retrieval_date` | date | yes | no | — | ISO 8601 date | Date source value was retrieved | ingest |
| `processing_lineage` | string | yes | no | — | — | Extraction/transformation steps | ingest |

### 5.3 `AQS-RAIN-IMD-DISTRICT`

Unique constraints: `observation_id`; `location_id + period_start + period_end`. Unit pair: `rainfall_value` → `rainfall_unit`. Temporal matching uses the explicit interval, not `observation_date`.

| Field | Type | Req. | Nullable | Unit | Constraint | Description | Provenance |
|---|---|---|---|---|---|---|---|
| `observation_id` | string | yes | no | — | pattern `^[A-Za-z0-9_.:-]+$` | Stable unique id for one rainfall record | generated during ingest |
| `dataset_id` | string | yes | no | — | pattern `^AQS-[A-Z]+-[A-Z0-9-]+(-v[0-9]+\.[0-9]+\.[0-9]+)?$` | Dataset version id used for this record | contract |
| `location_id` | string | yes | no | — | — | Station/district/grid id as published | source table |
| `observation_date` | date | yes | no | — | ISO 8601 date | Source-reported observation/publication date; not used alone for matching | source table |
| `period_start` | date | yes | no | — | ISO 8601 date | Inclusive start of accumulation interval | source metadata |
| `period_end` | date | yes | no | — | ISO 8601 date; not before `period_start` | Inclusive end of accumulation interval | source metadata |
| `longitude` | decimal | yes | no | degrees | [-180, 180] | Representative coordinate in declared CRS | source metadata |
| `latitude` | decimal | yes | no | degrees | [-90, 90] | Representative coordinate in declared CRS | source metadata |
| `crs` | string | yes | no | — | explicit EPSG/WKT | CRS identifier | dataset metadata |
| `rainfall_value` | decimal | yes | conditional | see `rainfall_unit` | finite; empty only for `INVALID`/`UNKNOWN` | Rainfall total for `[period_start, period_end]` | source table |
| `rainfall_unit` | string | yes | no | — | — | Unit from source | source table |
| `accumulation_period` | string | yes | no | — | `DAY`, `MONTH`, `SEASON`, `YEAR`, `UNKNOWN` | Category of the explicit interval; explicit dates take precedence | source metadata |
| `source_spatial_support` | string | yes | no | — | `STATION`, `DISTRICT_AGGREGATE`, `GRID`, `UNKNOWN` | Spatial support; controls allowable matching methods | source metadata |
| `quality_flag` | string | yes | no | — | `VALID`, `QUESTIONABLE`, `INVALID`, `UNKNOWN` | Value-required vs no-value flag (see §2.5) | source metadata |
| `missing_reason` | string | no | yes | — | controlled reason codes | Single code; valid only if all empty optional fields share it | producer |
| `missing_reason_map` | string | no | yes | — | JSON object of field→reason code | Per-field reasons when empty optional fields differ | producer |
| `source_reference` | string | yes | no | — | — | Exact source table/product id | producer |
| `retrieval_date` | date | yes | no | — | ISO 8601 date | Date source value was retrieved | ingest |
| `processing_lineage` | string | yes | no | — | — | Extraction/transformation steps | ingest |

### 5.4 Deferred schemas
`AQS-REF-HYDROGEOLOGY`: geometry model, CRS and attribute schema deferred until AQ-01/AQ-05. Minimum metadata when obtained: `geometry_type`, `crs`, `map_scale`, `source_year`, `license`, `source_reference`.
`AQS-REF-DEM`: raster handling and common grid deferred. Minimum metadata when obtained: `crs`, `native_resolution`, `nodata_value`, `product_version`, `source_reference`, `license`.

## 6. Spatial data requirements

1. CRS is mandatory per dataset and must be stored with the data; project CRS is `null`/PENDING. For InSAR, `platform`, `relative_orbit` and `pass_direction` are also mandatory so acquisition geometry is first-class metadata; the unique key includes the track.
2. Coordinates are x then y (longitude then latitude for geographic CRS) — PROPOSED; retain source order if different and document it.
3. W1 geometry representation is point coordinates plus identifiers. Polygon boundaries, raster grids and a common resolution are deferred to W2 after AQ-01.
4. Spatial matching requirements cannot be fixed before the pilot: they depend on boundary, well density, pixel size and DEM resolution. The protocol (§ its spatial section) lists candidate methods and their preconditions.
5. Every reprojection must be recorded in `processing_lineage` with source and target CRS; no silent reprojection.
6. Invalid coordinates are reported as `VR-005` errors with row numbers. No clamping, deletion or guessing.
7. Coordinate validity ranges in §2.3 are geometric sanity checks only; they do not prove a coordinate is inside the study area.

## 7. Temporal data requirements

1. ISO 8601; UTC preferred; date-only allowed with day precision and no invented timezone.
2. Acquisition date (SAR) is distinct from observation date (well) and accumulation interval (rainfall).
3. Source-reported cadence (about 4 well readings/year; Sentinel-1 revisit) is context only, not a verified local cadence.
4. Duplicate timestamps are evaluated using each dataset's declared unique constraints (§5) and reported with row numbers.
5. Missing temporal observations are flagged, not filled; gaps are reported with coverage statistics in later weeks.
6. Alignment rules (windows, aggregation, lags) are defined in the protocol, not in this contract, and are not executed in W1.

## 8. Data quality and integrity — validation rules

| Rule | Severity | Requirement |
|---|---|---|
| `VR-001` required_columns | ERROR | All required fields exist as columns. |
| `VR-002` unexpected_columns | WARNING | Undefined columns are reported, not silently ignored. |
| `VR-003` non_nullable_empty | ERROR | Non-nullable fields are non-empty in every row. |
| `VR-004` type_parse | ERROR | Values parse as declared type; non-finite numbers rejected. |
| `VR-005` coordinate_range | ERROR | `longitude`/`latitude` finite and within declared ranges. |
| `VR-006` allowed_values | ERROR | Categorical fields use declared allowed values. |
| `VR-007` pattern | ERROR | String fields with a pattern fully match it. |
| `VR-008` duplicate_key | ERROR | Declared unique constraints hold across all rows. |
| `VR-009` unit_pair_presence | ERROR | If a measurement value is present, its paired unit is present. |
| `VR-010` provenance_completeness | ERROR | Required dataset metadata and record provenance fields are present. |
| `VR-011` contract_internal_consistency | ERROR | Contract has unique dataset ids/field names, valid definitions and resolvable constraint fields. |
| `VR-012` value_quality_consistency | ERROR | Measurement value present for value-required flags; empty for no-value flags. |
| `VR-013` no_value_reason | ERROR | A no-value flag requires a reason in `missing_reason` or `missing_reason_map` for that value field. |
| `VR-014` dataset_id_match | ERROR | Row `dataset_id` equals the selected dataset (or `<id>-v<semver>` form). |
| `VR-015` period_order | ERROR | `period_end` is not before `period_start`; both are required for rainfall. |
| `VR-016` missing_reason_map | ERROR | Map parses as JSON object of valid reason codes and covers every empty optional field when more than one is empty. |

**Failure handling:** every failure is written to a structured report with `rule_id`, `severity`, `dataset_id`, row number (1-based data row), field name and message. Reports are JSON-serialisable. Inputs are never modified; problematic rows remain in the data and are listed in the report. A `ERROR` makes the report status `FAIL`; `WARNING` alone yields `PASS_WITH_WARNINGS`. No record is silently discarded.

## 9. Versioning convention

- Identifier: `AQS-DC`; version format `MAJOR.MINOR.PATCH` (SemVer-style).
- `0.x` denotes draft/pre-1.0; promotion to `1.0.0` requires a recorded decision at the 2026-12-06 gate.
- A version change is required when schema, units, geometry, temporal aggregation, processing, quality rules or validation logic change.
- Revision history:

| Version | Date | Change | Status |
|---|---|---|---|
| 0.9.0 | 2026-11-24 | Initial provisional contract: 5 dataset entries, 3 tabular schemas, 11 validation rules, pilot-dependent values marked PENDING | Draft for W1 review |
| 0.9.0 (revision 1) | 2026-11-27 | Unreleased draft corrections from PR review: value/quality semantics, InSAR acquisition geometry, explicit rainfall interval, row-level dataset id, per-field reason map; 16 validation rules | Draft for W1 review |

- Compatibility: changes to required fields, types, units or unique constraints are breaking; changes to descriptions or optional fields are minor. Dataset version lineage must record which contract version produced a dataset.

### Pending decisions affecting this contract
`AQ-01` pilot/boundary · `AQ-03` real reference data · `AQ-04` Sentinel-1 feasibility · `AQ-05` CRS/grid/units/formats/vocabularies · `AQ-06` validation protocol · `AQ-07` labels for modelling · `AQ-11` missing PDF. Full register: `AquaInSAR_W1/reports/W1_Project_Context_Map.md` and `docs/open-questions.md`.

## 10. Agreement with the machine-readable contract

The JSON companion is the canonical machine-readable definition. Dataset IDs, field names, types, required/nullable flags (including conditional nullability), allowed values, patterns, ranges, acquisition-geometry fields, rainfall interval fields, reason-map fields, unique constraints, unit pairs, validation rule IDs/severities, version and status are identical in both files. `tests/test_docs_consistency.py` checks this agreement automatically. If a review changes one representation, both must be changed in the same commit.

## 11. Known limitations

- All entries are prospective; no local data or scene manifest exists.
- Spatial, temporal and unit canonical values are intentionally pending; downstream work must not treat them as decided.
- This contract does not define validation, risk or forecast outputs.
- Field names are aligned with a read-only inspected bytecode artifact for continuity; that artifact is not executable evidence and is not a source of truth.
