# AquaInSAR Exploratory Comparison Protocol v1.0

**Protocol ID:** `AQS-ECP` · **Version:** `1.0.0` · **Date:** 2026-11-24
**Owner:** AC (Aishwary) · **Reviewer:** SJ · **Status:** Draft for W1 review
**Companion contract:** `AQS-DC` v0.9.0 (`../contracts/AquaInSAR_Data_Contract_v0.9.0.json` / `.md`)

> This is a **methodology document**, not a results report. No AquaInSAR comparison has been
> computed. No real data, scene manifest, deformation map or groundwater series exists in
> the repository. Nothing here authorises a prediction, validation or well-failure claim.

## 4.1 Research objective

### What is compared
For a pilot area still to be selected (AQ-01), the protocol compares:

- **Observations:** Sentinel-1-derived displacement values (`AQS-INSAR-S1-DISPLACEMENT`), each with acquisition date, pixel/station id, measurement convention, quality flag and uncertainty where available.
- **Reference measurements:** groundwater level/head at wells (`AQS-GW-CGWB-WELL`) and rainfall context (`AQS-RAIN-IMD-DISTRICT`), plus deferred geology/DEM context (`AQS-REF-HYDROGEOLOGY`, `AQS-REF-DEM`).

### Why the comparison matters
Groundwater observations can be sparse or delayed; crop greenness is a lagging indicator. Surface deformation may provide earlier regional information, but subsidence is indirect and has several possible causes. The comparison tests whether deformation carries information about groundwater conditions **in the selected setting and period**, not whether it does so universally.

### Research questions
- **RQ1 (descriptive):** What deformation, groundwater and rainfall observations are actually available for the pilot, with what coverage, quality and uncertainty?
- **RQ2 (association):** After explicit spatial/temporal matching, do displacement values covary with groundwater measurements or rainfall in the available sample?
- **RQ3 (qualification):** Under what geological, seasonal and data-quality conditions does the association weaken, reverse, or fail to appear?

### Definitions
- An **observation** is a value produced by a documented measurement or processing chain (e.g. one LOS displacement estimate for one pixel/acquisition).
- A **reference measurement** is an independent groundwater, rainfall or geological record used to interpret that observation. Source availability alone is not a reference measurement.
- An **exploratory association** is a documented relationship in the available sample; confounding remains possible.
- **Validation** requires an independent or otherwise suitable reference evaluated with stated scope, metric and uncertainty. **Prediction** requires an evaluated model with a target, horizon and held-out data. Neither is performed under this protocol.

### Conclusions this protocol can and cannot support

| Can support | Cannot support |
|---|---|
| Dataset availability, schema and quality descriptions | That aquifers are depleting, based on deformation alone |
| Coverage, missingness and uncertainty summaries | Causation between pumping, compaction and subsidence |
| Exploratory covariation in a defined sample | An individual well's failure date or "days to failure" |
| Negative/inconclusive findings and data gaps | Operational warnings, validated risk classes or forecasts |
| A justified decision that modelling is not warranted | Generalisation to other districts or periods |

## 4.2 Data preparation (prospective; not executed in W1)

1. **Dataset identification.** Use only dataset IDs defined in the contract (`AQS-DC` v0.9.0). Do not merge a new source without a contract version change.
2. **Source verification.** Record source organisation, exact publication/product id, retrieval date, license and URL/file; preserve original files. Source existence is not data availability (see context map, finding 7).
3. **Ingestion assumptions.** Pilot boundary, CRS, grid, cadence and canonical units are **PENDING**; any ingest performed before AQ-05 must carry those as explicit run-level assumptions, not as contract facts.
4. **Schema consistency.** Run `AquaInSAR_W1/src/aquainsar_w1/contract_tools.py` validation before any analysis. `ERROR` findings block analysis until explained; `WARNING` findings are documented with a decision.
5. **Missing-data treatment.** Empty fields remain missing. No imputation, no numeric sentinels, no row deletion. Missingness is reported with counts and reason codes.
6. **Unit harmonisation.** No unit conversion is performed in this protocol. If conversion is needed, it requires a new contract version with formula and lineage. Depth-vs-head and LOS-vs-vertical distinctions are preserved, not collapsed.
7. **Spatial standardisation.** Declare CRS and coordinate order; do not reproject until the target CRS is decided. Record any reprojection with source/target CRS and method.
8. **Temporal standardisation.** Convert timestamps to ISO 8601 as recorded in source, preserving date-only precision; do not invent midnight or timezone for date-only records.
9. **Quality filtering.** Filtering is analysis-level and must be logged: rule, affected rows, rationale and analyst. It must not mutate source tables. Comparing only "VALID" rows is allowed only if the excluded rows are reported: it changes the sample and must be stated.

## 4.3 Spatial comparison methodology

No method is selected in W1. The choice depends on the pilot boundary, CRS, well coordinates, pixel geometry and resolution, all unresolved. Candidates and their preconditions:

| Method | Appropriate when | Procedure (prospective) | Main limitation |
|---|---|---|---|
| **Point-in-pixel sampling** | Displacement is a raster/grid product and wells are point locations with trustworthy coordinates and shared CRS | Sample displacement value at well coordinate; record grid id and distance to pixel centre | Point supports differ (well screen vs surface pixel); scale mismatch |
| **Buffer matching** | Coordinates are approximate or well/pixel support differs; buffer distance is justified by positional accuracy, not chosen to maximise correlation | Define buffer from documented location uncertainty; aggregate displacement values inside it; report count and distances | Result depends strongly on buffer size; must be pre-specified |
| **Zonal statistics / aggregation** | A versioned pilot boundary or block polygons exist and the question is area-level | Aggregate displacement by polygon (mean/median/count), preserve within-zone spread; compare with polygon-level groundwater summaries | Modifiable areal unit problem; district blocks may not align with aquifers |
| **Grid-based matching** | Both datasets can be referenced to a declared common grid with documented resampling | Assign records to grid cells; report cell coverage and resampling method | Resampling cannot add source resolution; false precision risk |
| **Spatial interpolation** | Only with dense, spatially representative point data and a justified model (e.g. variogram-based), evaluated on held-out points | Fit interpolation on training points; report held-out error before using it for matching | Can manufacture smooth fields from sparse wells; prohibited if density/CRS unverified |

**Rules:** interpolation is not used when well density or CRS is unverified (G-02, G-03); all methods must report spatial coverage and mismatch explicitly; matching parameters are fixed before looking at outcomes; any changed parameter is logged as a new exploratory run, not silently tuned.

## 4.4 Temporal comparison methodology

| Method | Appropriate when | Procedure (prospective) | Main limitation |
|---|---|---|---|
| **Exact-date matching** | Both sources share a verified timestamp convention and comparable cadence | Join on identical ISO 8601 date/interval | Rarely feasible: SAR revisit and ~4 well readings/year differ |
| **Temporal window** | Cadence differs but a scientifically justified window exists (e.g. well reading ± N days) | Pre-register N from source cadence, not from outcomes; keep all candidate pairs and report unmatched records | Window choice changes apparent association; asynchronous records are not simultaneous |
| **Aggregation** | Comparing seasonal or annual behaviour | Aggregate to a declared interval using source semantics; report aggregation and missing intervals | Aggregation hides short events; season definitions require IMD/CGWB confirmation |
| **Lag analysis** | A physical delay is hypothesized (e.g. pumping → compaction → water-level response) | Pre-register a small set of lags with hydrogeological rationale; report all tested lags, not only the best | Multiple lags inflate false positives; exploratory only |
| **Time-series alignment** | Both series have sufficient length and coverage after matching | Align by declared date/interval; report overlap length, gaps and counts | Short overlap or seasonality can dominate results |

**Acquisition vs observation:** `acquisition_date` for SAR and `observation_date` for wells are distinct fields in the contract. The displacement reference date, where present, must be recorded. Date-only well records retain day precision; no timezone is inferred. Asynchronous observations cannot establish simultaneity, and any association must be described with the actual dates and lags used.

## 4.5 Exploratory statistical methodology

All methods below are descriptive/exploratory. No hypothesis is confirmed by them. Every run records inputs, parameters, exclusions and outputs.

| Method | Purpose | Required inputs | Assumptions | Expected output | Interpretation | Limitations |
|---|---|---|---|---|---|---|
| Descriptive statistics | Establish scale, spread and coverage | One declared numeric field with quality flags | Units known; values are measurements | Count, min/max, mean/median, quantiles | Describes the available sample only | Sensitive to outliers and unequal coverage |
| Distribution analysis | Inspect shape and anomalies | Same as above | Comparable units within a field | Histogram/violin-style summary, count by bin | Reveals skew, clusters, implausible values | Does not identify cause of anomalies |
| Missingness analysis | Quantify gaps and bias risk | Full tables plus reason codes | Missingness is informative, not ignorable | Missing count/% by field, time, space | Shows where inference would be unsupported | Cannot recover missing values |
| Scatter plots | Visualise paired values | Matched pairs with explicit keys | Matching already documented | Scatter with quality/colour encoding | Suggests association or non-linearity | Visual impressions are not tests |
| Spatial distribution plots | Inspect geography of observations and gaps | Coordinates, CRS, boundary | Coordinates valid and CRS declared | Point/raster map with coverage masks | Shows clustering, urban bias, no-data areas | Map appearance can overstate evidence |
| Temporal trend inspection | See direction over time | Date/interval and value | Coverage reported; seasonality considered | Time series with gaps shown | Suggests trend or seasonal cycle | Short series and gaps can mimic trends |
| Pearson correlation | Measure linear association | ≥ 2 paired numeric variables | Approximate linearity, finite variance, no dominating outliers; pairs independent enough for description | r with n and coverage | Strength of *linear* sample association | Sensitive to outliers; no causation; not valid for sparse/asynchronous pairs without described matching |
| Spearman correlation | Measure monotonic association | Same as above | Monotonic relation; ordinal-safe ranks | rho with n and coverage | More robust to non-linearity/outliers than Pearson | Still sample association; ties and seasonality matter |

**Decision rules for use**
1. Compute correlations only after the spatial/temporal matching rule is fixed and logged.
2. Report `n`, coverage, dates, units, quality exclusions and the matching rule alongside every coefficient.
3. Report **all** pre-registered comparisons, including weak or null ones. Do not select the best-looking lag, window or buffer after seeing results.
4. Do not treat p-values as confirmation of a physical mechanism; with exploratory samples they are descriptive, not confirmatory.
5. Association ≠ prediction ≠ validation. Any later risk indicator must satisfy AQ-07 label requirements and the validation protocol (AQ-06) before such language is used.
6. A negative or inconclusive association is a valid result and must be preserved.

## 4.6 Uncertainty and limitations

| Factor | Status in project evidence | Effect on comparison |
|---|---|---|
| Deformation measurement uncertainty, atmosphere, orbit, unwrapping | Potential, method-level (`docs/independent-research.md`) | Adds noise/bias to displacement; require quality flags and uncertainty fields |
| LOS vs vertical displacement | Confirmed method limitation | A line-of-sight rate is not automatically vertical subsidence; convention must be explicit |
| Crop/vegetation decorrelation | Potential, source-supported general risk; not measured locally | May create gaps exactly in agricultural areas; require coherence coverage by season |
| Groundwater datum, screen depth, aquifer metadata | Confirmed gap (G-03) | Depth/head values may not be comparable between wells |
| Spatial support mismatch (well vs pixel vs district) | Confirmed from source descriptions | Aggregation/buffer choices materially change results |
| Temporal mismatch (~4 well readings/year vs SAR revisit) | Source-reported, not locally verified | Asynchrony limits exact-date matching and lag interpretation |
| Extraction-stage categories | Confirmed not a water-level trend (MF inventory) | Screening context only; never used as validation label |
| GRACE coarse storage signal | Confirmed context-only | Cannot resolve an individual well or small district |
| Sampling bias (urban persistent scatterers, accessible wells) | Potential, documented in research notes | Rural agricultural inference may be unsupportable |
| Missing data and short overlap | Likely; unverified | May force an inconclusive result |

Each analysis output must carry: sample size, coverage, excluded rows/dates, stated uncertainty or `NOT_QUANTIFIED`, and a scope statement (region and period). If compatible reference data do not exist, the correct output is a feasibility gap, not a validation claim.

## 4.7 Reproducibility

- **Required inputs:** contract JSON (`AQS-DC` v0.9.0), versioned source tables, source manifests, pilot boundary geometry when decided, and a dated run configuration.
- **Processing assumptions:** recorded explicitly at run start, including pilot-dependent values still pending.
- **Software dependencies:** Python 3.10+; W1 validator uses only the standard library. Later notebook-based work may add pandas/matplotlib with pinned versions captured in the run record.
- **Configuration:** matching method, window/lag definitions, quality rules, exclusions and output naming stored in a versioned config file; no hidden defaults.
- **Processing sequence:** contract validation → source verification → schema ingest → quality report → spatial/temporal matching → descriptive statistics/plots → scoped interpretation → QA review.
- **Output naming:** `AQS_W<week>_<dataset_or_analysis>_<YYYYMMDD>_v<semver>`; derived outputs store input dataset ids/versions, code version, parameters, operator and processing date.
- **Versioning:** analysis code and config are committed together with outputs; raw sources remain immutable where terms permit.
- **Provenance:** every plotted or tabulated value traceable to dataset id, source reference, quality flag and run id.
- **Execution record template:** run id, date/time, operator, code commit, contract version, input file hashes, configuration, command, output paths, issues found, decisions made, reviewer.
- **No fabricated results:** synthetic fixtures may test software only; they must be labelled `SYNTHETIC_TEST` and excluded from interpretation.

## 4.8 W1 status and handover

No analysis in §§4.2–4.7 has been executed for AquaInSAR data in W1. The validator implemented this week checks contract structure and CSV schema/quality only; it does not perform matching, statistics, conversion or interpretation. W3 implements the joined-data workflow after AQ-01, AQ-03 and AQ-04 supply real inputs; W4 decides baseline vs no-model; validation and forecasting remain gated by AQ-06/AQ-07.
