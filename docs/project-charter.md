# AquaInSAR Project Charter

## Purpose

This charter records the project definition and operating scope provided by SJ and the team, plus the planning decisions made in the repository. It is a living explanation of what AquaInSAR is intended to investigate. It does not claim that planned technical work has been completed.

## Project identity

| Item | Current definition |
|---|---|
| Project | AquaInSAR |
| Competition | Conrad Challenge |
| Team | The Oopsies |
| Category | Aerospace & Aviation |
| Innovation classification | New, original concept, as identified in the project context |
| Initial geography | An agricultural region in Uttar Pradesh, India; the pilot district is not yet selected |
| Working deadline | January 7, 2027, based on the team's stated January 7 deadline and the current planning year; exact cutoff time and timezone require verification |

## Problem

Farmers and agricultural communities can depend heavily on groundwater yet learn that access is worsening only after wells become less productive or fail. Groundwater observations can be sparse or delayed. Crop-vegetation monitoring may reveal visible stress after groundwater pressure has already affected farming decisions.

AquaInSAR explores whether satellite-observed ground deformation, combined with local groundwater, rainfall, and geological information, can contribute earlier regional groundwater-stress information.

## Proposed solution

The planned end-to-end workflow is:

1. Acquire Sentinel-1 synthetic aperture radar (SAR) imagery for a selected study area.
2. Process suitable imagery with an interferometric workflow to estimate ground deformation and its quality.
3. Assemble groundwater-level, rainfall, geological, seasonal, and other relevant reference information.
4. Align the observations in space and time and assess the relationship between deformation and groundwater conditions.
5. Develop a simple stress indicator or risk classification only if the data support it; report uncertainty and limitations.
6. Present supported observations through a geospatial dashboard and, if appropriate, demonstrate a clearly labeled alert prototype.

## Research question and intended contribution

**Research question:** In a selected Uttar Pradesh agricultural region and study period, do Sentinel-1-derived deformation observations provide useful evidence about groundwater stress when evaluated alongside groundwater and environmental reference data?

The project must be able to support either a positive, negative, or inconclusive result. A scientifically useful outcome may be evidence that deformation is not a reliable groundwater-stress indicator in the selected setting, or that available ground data are insufficient to evaluate it.

## Users and beneficiaries

Potential users include groundwater-dependent farmers, agricultural cooperatives, irrigation authorities, state groundwater departments, crop insurers, and agricultural researchers. These are proposed customer and stakeholder groups, not confirmed customers. User needs, trust, willingness to pay, and preferred delivery channels remain to be tested.

## Scope through the stated deadline

The weekly plan targets a defensible prototype demonstration: select a pilot using evidence, establish data availability, produce a reproducible deformation observation if feasible, compare it with real reference data, represent uncertainty, and show supported outputs in a dashboard. The plan includes a documented feasibility result if usable data or processing conditions cannot be obtained in time.

The deadline does not imply that AquaInSAR will establish a universal subsidence-groundwater relationship, predict an individual well failure, or prove measurable community impact. Such claims require stronger evidence and validation than the current project record contains.

## Business hypothesis

The initial business hypothesis, not validated market evidence, is that cooperatives, groundwater agencies, insurers, researchers, or other institutions may value regional groundwater-risk information. Potential channels include partnerships, research pilots, dashboards, and SMS/WhatsApp alerts. Possible revenue models include subscriptions, regional reports, enterprise analytics, sponsored pilots, or research partnerships. Pricing, demand, deployment cost, and willingness to pay require customer discovery and pilot evidence.

Potential success measures include deformation-estimation quality against suitable references, quality of the groundwater comparison, risk-warning precision and lead time where labels exist, user adoption, and independently measurable impact. No baseline values or achieved metrics have been recorded.

## Execution milestones

1. **Research foundation:** choose a defensible pilot, review evidence, inventory datasets, state the hypothesis, design validation, and draft the data contract.
2. **Technical prototype:** acquire and process Sentinel-1 imagery, assemble reference records, produce preliminary observations, develop initial analysis, and establish dashboard architecture.
3. **Validation and integration:** compare satellite observations with ground data, evaluate methods and uncertainty, and connect supported outputs to the dashboard.
4. **Demonstration and competition readiness:** prepare an end-to-end demonstration, methodology and findings, business assumptions, presentation, and technical answers.

The detailed dated tasks are in the [weekly deliverables plan](../tasks/plan.md).

## Evidence status as of November 20, 2026

| Item | Status |
|---|---|
| Concept, scientific caveat, initial geography, and team vertical definitions | Provided in the team's master project context |
| Five named role assignments | Confirmed by SJ in this conversation; see [team and ownership](team-and-ownership.md) |
| Weekly work schedule through January 7 | Planned in `tasks/plan.md`; all checklist items begin Not Started |
| Pilot region, reference datasets, and actual Sentinel-1 scene set | Not selected or evidenced in the current repository |
| Processing pipeline, deformation maps/time series, validated risk model, dashboard, or alert service | Not evidenced as implemented or tested |
| Independent validation or user research results | Not evidenced as completed |

The repository contains `Project_Details.pdf`, but its contents were not incorporated into this charter and must be reviewed before treating it as a source for competition requirements or project facts.

## Related documents

- [Team and ownership](team-and-ownership.md)
- [Research and validation](research-and-validation.md)
- [Data contract](data-contract.md)
- [Open questions](open-questions.md)
- [Evidence-first scope decision](decisions/0001-evidence-first-claims.md)
