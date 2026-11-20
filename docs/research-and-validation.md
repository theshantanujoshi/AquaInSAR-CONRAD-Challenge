# Research and Validation Approach

## Purpose and claim boundary

This explanation records the proposed scientific approach. It is not evidence that the work has been performed. AquaInSAR treats surface deformation as an indirect observation that may be associated with groundwater stress under some geological and hydrological conditions. Subsidence alone does not establish aquifer depletion, causation, or an individual well's future failure.

Deformation may also reflect geology, soil compaction, tectonic activity, seasonal movement, atmospheric artefacts, decorrelation, processing noise, or other factors. The team must investigate these alternatives and report uncertainty.

## Testable hypothesis

For a selected agricultural area and period in Uttar Pradesh, satellite-derived deformation may covary with measured groundwater conditions after accounting for temporal coverage, seasonal patterns, geological setting, and observation quality.

The hypothesis is not yet tested. The study region, timeframe, actual datasets, spatial/temporal matching rules, and thresholds remain to be determined from evidence.

## Proposed workflow

1. **Screen candidate regions.** Compare groundwater-stress evidence, well-monitoring and rainfall records, aquifer/geological information, Sentinel-1 coverage, and feasibility of ground validation. SJ records the decision and alternatives.
2. **Inventory source data.** MF records source, units, geography, date range, monitoring density, missingness, and limitations for groundwater, rainfall, and hydrogeological information.
3. **Acquire and process radar data.** SM records Sentinel-1 scenes, acquisition geometry, preprocessing, interferometric choices, quality/coherence information, and processing configuration.
4. **Check data compatibility.** AC coordinates shared fields and quality checks with all verticals. Spatial and temporal alignment must be documented rather than assumed.
5. **Compare observations.** Define a baseline that compares deformation with groundwater/environmental records, including plausible lag and seasonal effects when data allow. MF leads the ground-reference method; AC implements reproducible analysis; SM explains deformation uncertainty.
6. **Evaluate before classifying.** Use descriptive analysis first. Add risk classification or forecasting only if sufficient, representative reference labels exist and evaluation can address generalization and false alarms.
7. **Communicate evidence.** AP presents supported outputs and uncertainty in the dashboard. Each layer shows dates, units, provenance, quality, and limitations.

## Evidence levels

Keep these statements distinct in research notes, dashboards, and competition materials:

| Level | Meaning | Example of an acceptable statement |
|---|---|---|
| Planned | Work is proposed but not performed. | “The team plans to compare deformation with groundwater records.” |
| Observed | A specific dataset and method produced a measurement. | “This processing run estimated displacement for these dates and pixels.” |
| Associated | A documented analysis found a relationship in the available sample. | “In this study period, the measured variables covaried; confounding remains possible.” |
| Validated | An independent or suitable reference evaluation supports stated performance within a defined scope. | State the reference, sample, metric, uncertainty, and geographic/temporal scope. |
| Predicted | A model forecasts a defined outcome and has been evaluated on suitable held-out data. | State target, horizon, calibration, error modes, and limits. |

Never promote a planned, observed, or associated result to a validated prediction without the evidence required at the higher level.

## Validation requirements

- Compare satellite-derived displacement with independent or otherwise suitable ground references where available; document reference limitations.
- Match records across space and time with explicit rules, units, and coverage reporting.
- Check seasonal effects, geology, groundwater abstraction context, atmospheric artefacts, coherence/decorrelation, and other plausible explanations.
- Report sample size, missingness, uncertainty, and any excluded areas or dates.
- Evaluate false positives, false negatives, and warning lead time only when defensible labels and event definitions exist.
- Preserve negative and inconclusive findings. If compatible ground data do not exist, report a feasibility gap rather than claiming validation.

## Proposed research geography

The team intends to study an agricultural region in Uttar Pradesh. No district or aquifer has been selected. Selection should be based on groundwater-stress evidence, accessible monitoring data, Sentinel-1 suitability, geological relevance, and practical validation opportunities—not convenience or an unsupported assumption. See the [weekly plan](../tasks/plan.md) and [open questions](open-questions.md).

## Current evidence status

As of November 20, 2026, the repository does not contain acquired study datasets, scene manifests, processed deformation outputs, comparison results, model evaluations, field observations, or user-research findings. The weekly plan marks the related work as Not Started. This section should be updated only when artifacts and sources have been reviewed.
