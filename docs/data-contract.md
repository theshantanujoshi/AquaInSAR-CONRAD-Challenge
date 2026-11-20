# Shared Data Contract (Draft)

**Status:** Draft requirements. AC coordinates the final contract with MF, SM, and AP; no pilot-specific CRS, grid, resolution, exchange format, or canonical physical units have been approved yet.

## Purpose

The contract prevents satellite, hydrogeology, modelling, and product work from silently changing coordinate systems, timestamps, units, missing-value meanings, or uncertainty. Each dataset retains its source provenance and quality information through the pipeline.

## Contract requirements

| Field | Draft rule | Decision status |
|---|---|---|
| Dataset identity and version | Assign a stable dataset ID and version to every source and derived dataset. Preserve a link to the exact version used in analysis. | Required; naming convention TBD by AC. |
| Provenance | Record publisher/provider, source title or identifier, access location, retrieval date, license/terms if known, and transformations. | Required; capture details per source. |
| Geographic boundary | Record study boundary as a versioned geometry and identify its CRS. Preserve original source geometry where supplied. | Pilot boundary and storage format TBD after region selection. |
| Coordinate reference system | Declare CRS for every geometry/raster; never assume it from coordinates. Document every reprojection. | Specific project CRS TBD after data inventory. |
| Spatial resolution | Record native resolution and any resampling/interpolation method. Do not imply resampled data contain finer source information. | Common grid/resolution TBD based on sources and task. |
| Temporal coverage and resolution | Record observation/acquisition dates, source cadence, gaps, and any aggregation/windowing. Document matching and resampling methods. | Study period and common cadence TBD after data inventory. |
| Timestamp convention | Proposed canonical representation is ISO 8601 in UTC for machine-readable timestamps; retain original source value/timezone and note date-only records. | Proposed; AC confirms in contract v1. |
| Measurement and units | Every variable includes a value, variable name, and unit. Preserve source units; record conversions and canonical units per variable. | Required; canonical variable units TBD from source inventory. |
| Missing data | Use explicit null/NoData plus a reason where known (e.g., not measured, masked, unavailable, invalid). Zero is a measurement, not a missing-data code. Record any imputation separately. | Required; reason-code vocabulary TBD. |
| File format | Preserve original source files. Choose interoperable formats for processed vectors, rasters, and tables based on the actual toolchain; record format and schema. | Exchange formats TBD; no toolchain is established in the repository. |
| Quality indicators | Carry source-appropriate quality fields, masks, flags, and processing notes. Examples may include interferometric coherence or groundwater-record quality, where supplied. | Required; field definitions TBD per dataset. |
| Uncertainty | Store uncertainty or confidence information with the measurement when available; describe method and units. If unavailable, state “not quantified” instead of implying certainty. | Required; method is dataset/model-specific. |
| Derived data lineage | Record input dataset versions, code/configuration version, processing date, parameters, and operator for every derived output. | Required; implementation and storage convention TBD. |

## Minimum logical record

The following fields describe a conceptual record, not a finalized file schema:

```text
dataset_id
dataset_version
record_id
source_reference
variable
value
unit
observation_time_or_interval
geometry_or_grid_reference
crs
native_spatial_resolution
quality_flag_or_mask
uncertainty_value_and_method
missing_reason
processing_lineage
```

Applicability depends on the data type. Raster products may express geometry and value through a georeferenced grid rather than repeating these fields per pixel. This example is illustrative and is not a runnable schema.

## Versioning and change control

- Keep raw source data immutable where access terms permit; store derived data separately.
- Increment a dataset version when schema, units, geometry, temporal aggregation, processing, or quality rules change.
- Record changes and downstream consumers in a changelog or manifest.
- Agree on interface changes with affected vertical owners before integration; update the schema and acceptance checks together.

## Decisions needed for contract v1

1. Pilot region geometry and CRS.
2. Project study period and temporal matching rule.
3. Source-specific canonical variables and units.
4. Common grid/resolution, if any, with justified resampling rules.
5. Processed file formats compatible with SM's pipeline and AP's dashboard.
6. Missing-value and quality-flag vocabularies.
7. Dataset naming and versioning convention.

AC owns coordinating contract v1; MF and SM supply domain/source fields, AP confirms product-consumption needs, and SJ reviews cross-vertical decisions. The planned dates are in [tasks/plan.md](../tasks/plan.md).
